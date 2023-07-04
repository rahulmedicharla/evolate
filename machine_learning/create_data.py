import csv
import random

# Define the data structures and their corresponding search algorithms
data_structures = {
    'Singly Linked List': 'Iterative Search',
    'Sequence - Ordered List': 'Binary Search',
    'Tree Map': 'DFS',
    'Hash Map': 'Hash Algorithm'
}

# Define the weights for the efficiency scoring function
weights = {
    'Total Node Length': 0.15,
    'Insertion/Deletion Frequency': 0.15,
    'Search Randomness': 0.64
}

threshold = .2


def select_data_structure(features, weights):
    if features["Search Randomness"] < 0:
        features["Total Node Length"] = -features["Total Node Length"]
        weights["Total Node Length"] = .26
        weights["Insertion/Deletion Frequency"] = .1
    else:
        features["Total Node Length"] = -features["Total Node Length"]
        weights["Total Node Length"] = .13
        weights["Insertion/Deletion Frequency"] = .23

    calculated_score = features["Search Randomness"] * weights["Search Randomness"] + features["Insertion/Deletion Frequency"] * weights["Insertion/Deletion Frequency"] + features["Total Node Length"] * weights["Total Node Length"]

    if calculated_score > 0 and calculated_score > threshold:
        return "Sequence"
    if calculated_score > 0 and calculated_score < threshold:
        return "Tree Map"
    if calculated_score < 0 and calculated_score < -threshold:
        return "Singly Linked List"
    if calculated_score < 0 and calculated_score > -threshold:
        return "Hash Map"
    
    return "Tree Map"
    

def generate_data_csv(filename, num_data_points):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([
            'Total Node Length',
            'Insertion/Deletion Frequency',
            'Search Randomness',
            'Data Structure'
        ])

        for _ in range(num_data_points):
            # Generate random values for the features
            total_node_length = random.uniform(0, 1)
            insertion_deletion_freq = random.uniform(0, 1)
            search_randomness = random.uniform(-.25,.25)
            
            # Create a dictionary of the features
            features = {
                'Total Node Length': total_node_length,
                'Insertion/Deletion Frequency': insertion_deletion_freq,
                'Search Randomness': search_randomness
            }

            # Calculate the recommended data structure based on the efficiency scores
            recommended_data_structure = select_data_structure(features, weights)

            # Write the data point to the CSV file
            writer.writerow([
                total_node_length,
                insertion_deletion_freq,
                search_randomness,
                recommended_data_structure
            ])

    print(f"Data saved to {filename}.")


# Usage example
generate_data_csv('machine_learning/data/data.csv', 1000000)
