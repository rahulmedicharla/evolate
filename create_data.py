import csv, random, time
from data_types import DataType
from data_structures.evolate import Evolate
from fractions import Fraction

class GenerateData():

    def __init__(self, file_path, iterations):
        self.file_path = file_path
        self.iterations = iterations

    def generate(self):

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
                insertion_deletion_freq = round(random.uniform(0, 1), 3)
                search_randomness = round(random.uniform(0,.48), 3)
                mean = False
                key_list = []
                fraction = Fraction(insertion_deletion_freq).limit_denominator()
                run_times = []
                for type in DataType:    
                    start_time = time.time()
                    struct = Evolate(type, data_creation=True)

                    for add in range(0, fraction.numerator):
                        struct.add(add)

                    length = struct.get_length()
                    if not mean:
                        mean = random.randint(0, length)
                        key_list = [round(random.normalvariate(mean, search_randomness)) for _ in range(fraction.denominator - fraction.numerator)]
                    for key in key_list:
                        struct.get(key)
                    
                    end_time = time.time()
                    run_times.append({
                        "Size" : struct.get_size(),
                        "Insertion/Deletion Frequency" : insertion_deletion_freq,
                        "Search Randomness" : search_randomness,
                        "Search Prediction" : mean,
                        "Data Structure" : str(type).split(".")[1],
                        "Runtime" : end_time - start_time
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
    create_data = GenerateData("machine_learning/data/temp.csv", 100000)
    create_data.generate()
    
