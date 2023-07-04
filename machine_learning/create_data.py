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
    'Average Node Size': 0.1,
    'Total Node Size': 0.15,
    'Total Node Length': 0.05,
    'Insertion/Deletion Frequency': 0.2,
    'Search Frequency': 0.3,
    'Update Frequency': 0.2
}


def select_data_structure(features, weights):
    # Define the ranges and corresponding data structures
    ranges = [
        (0, 0.25, 'Singly Linked List'),
        (0.25, 0.5, 'Sequence'),
        (0.5, 0.75, 'Tree Map'),
        (0.75, 1.0, 'Hash Map')
    ]

    # Calculate the resulting value based on the features and their weights
    result = sum(features[feature] * weights[feature] for feature in features)

    # Find the data structure that corresponds to the range of the resulting value
    for range_start, range_end, data_structure in ranges:
        if range_start <= result < range_end:
            return data_structure

    # If no range matches, return a default data structure
    return 'Singly Linked List'  # Or any other default data structure


def generate_data_csv(filename, num_data_points):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([
            'Average Node Size',
            'Total Node Size',
            'Total Node Length',
            'Insertion/Deletion Frequency',
            'Search Frequency',
            'Update Frequency',
            'Data Structure'
        ])

        for _ in range(num_data_points):
            # Generate random values for the features
            average_node_size = random.uniform(0, 1)
            total_node_size = random.uniform(0, 1)
            total_node_length = random.uniform(0, 1)
            insertion_deletion_freq = random.uniform(0, 1)
            search_freq = random.uniform(0, 1)
            update_freq = random.uniform(0, 1)

            # Create a dictionary of the features
            features = {
                'Average Node Size': average_node_size,
                'Total Node Size': total_node_size,
                'Total Node Length': total_node_length,
                'Insertion/Deletion Frequency': insertion_deletion_freq,
                'Search Frequency': search_freq,
                'Update Frequency': update_freq
            }

            # Calculate the recommended data structure based on the efficiency scores
            recommended_data_structure = select_data_structure(features, weights)

            # Write the data point to the CSV file
            writer.writerow([
                average_node_size,
                total_node_size,
                total_node_length,
                insertion_deletion_freq,
                search_freq,
                update_freq,
                recommended_data_structure
            ])

    print(f"Data saved to {filename}.")


# Usage example
generate_data_csv('machine_learning/data/data.csv', 100000)
