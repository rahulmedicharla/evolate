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
    'Insertion/Deletion Frequency': 0.25,
    'Search Prediction': 0.35,
    'Search Density': 0.25
}


def select_data_structure(features, weights):
    # Define the ranges and corresponding data structures
    pass
    

def generate_data_csv(filename, num_data_points):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([
            'Total Node Length',
            'Insertion/Deletion Frequency',
            'Search Predicition',
            'Search Density',
            'Data Structure'
        ])

        for _ in range(num_data_points):
            # Generate random values for the features
            total_node_length = random.uniform(0, 1)
            insertion_deletion_freq = random.uniform(0, 1)
            search_prediction = random.uniform(0,1)
            search_density = random.uniform(0,1)
            
            # Create a dictionary of the features
            features = {
                'Total Node Length': total_node_length,
                'Insertion/Deletion Frequency': insertion_deletion_freq,
                'Search Prediction': search_prediction,
                'Search Density': search_density
            }

            # Calculate the recommended data structure based on the efficiency scores
            recommended_data_structure = select_data_structure(features, weights)

            # Write the data point to the CSV file
            writer.writerow([
                total_node_length,
                insertion_deletion_freq,
                search_prediction,
                search_density,
                recommended_data_structure
            ])

    print(f"Data saved to {filename}.")


# Usage example
generate_data_csv('machine_learning/data/data.csv', 3)
