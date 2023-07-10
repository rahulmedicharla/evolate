import csv, random, time
from data_types import DataType
from data_structures.evolate import Evolate
from fractions import Fraction

class GenerateData():

    def __init__(self, file_path, iterations):
        self.file_path = file_path
        self.iterations = iterations

    def generate_algorithmic(self):
        with open(self.file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([
                'Size',
                'Insertion/Deletion Frequency',
                'Search Randomness',
                'Search Prediction',
                'Data Structure'
            ])

            weights = {
                'Search Prediction': 0.005,
                'Insertion/Deletion Frequency': 0.395,
                'Search Randomness': 0.6
            }

            threshold = .2


            for i in range(self.iterations):
                print("Iter: " + str(i))
                # Generate random values for the features
                insertion_deletion_freq = round(random.uniform(0, 1), 3)
                search_randomness = round(random.uniform(-.25,.25), 3)
                search_prediction = round(random.uniform(0,1), 3)

                if search_randomness <= 0:
                    insertion_deletion_freq = -insertion_deletion_freq

                calculated_score = search_randomness * weights["Search Randomness"] + insertion_deletion_freq * weights["Insertion/Deletion Frequency"] + search_prediction * weights["Search Prediction"]
                

                if insertion_deletion_freq < 0:
                    insertion_deletion_freq = -insertion_deletion_freq

                data_structure = ""
                if calculated_score > 0 and calculated_score > threshold:
                    data_structure = "SEQUENCE"
                elif calculated_score > 0 and calculated_score < threshold:
                    data_structure =  "TREE_MAP"
                elif calculated_score < 0 and calculated_score < -threshold:
                    data_structure = "SINGLY_LINKED_LIST"
                else:
                    data_structure =  "HASH_MAP"
                                    
                # Write the data point to the CSV file
                
                writer.writerow([
                    insertion_deletion_freq * 1000 * 28,
                    insertion_deletion_freq,
                    search_randomness,
                    search_prediction,
                    data_structure
                ])

        print(f"Data saved to {self.file_path}.")


    def generate_actual(self):

        with open(self.file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([
                'Size',
                'Insertion/Deletion Frequency',
                'Search Randomness',
                'Search Prediction',
                'Data Structure'
            ])

            for i in range(self.iterations):
                print("Iter: " + str(i))
                # Generate random values for the features
                insertion_deletion_freq = int(round(random.uniform(0, 1), 3) * 1000)
                search_randomness = round(random.uniform(0,.48), 3)
                search_prediction = round(random.uniform(0,1), 3)


                mean = round(search_prediction * insertion_deletion_freq)
                key_list = [round(random.normalvariate(mean, search_randomness)) for _ in range(1000 - int(insertion_deletion_freq))]
                run_times = []

                for type in DataType:    
                    struct = Evolate(type, data_creation=True)

                    start_time = time.time()

                    for i in insertion_deletion_freq:
                        struct.add(i)

                    for key in key_list:
                        struct.get(key)
                    
                    end_time = time.time()

                    run_times.append({
                        "Size" : struct.get_size(),
                        "Insertion/Deletion Frequency" : insertion_deletion_freq,
                        "Search Randomness" : search_randomness,
                        "Search Prediction" : mean,
                        "Data Structure" : str(type).split(".")[1],
                        "Runtime" : (end_time - start_time)
                    })

                sorted_runtimes = sorted(run_times, key=lambda x: x['Runtime'])
                
                # Write the data point to the CSV file
                writer.writerow([
                    sorted_runtimes[0]["Size"],
                    sorted_runtimes[0]["Insertion/Deletion Frequency"],
                    sorted_runtimes[0]["Search Randomness"],
                    sorted_runtimes[0]["Search Prediction"],
                    sorted_runtimes[0]["Data Structure"],
                ])

        print(f"Data saved to {self.file_path}.")


# Usage example
if __name__ == '__main__':
    create_data = GenerateData("machine_learning/data/algorithmic_data.csv", 200000)
    # create_data.generate_actual()
    create_data.generate_algorithmic()
    
