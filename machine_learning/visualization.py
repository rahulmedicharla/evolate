import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('machine_learning/data/algorithmic_data.csv')

df["Cross 1"] = df["Insertion/Deletion Frequency"] 
df["Cross 2"] = df["Search Randomness"]

color_map = {
    'SINGLY_LINKED_LIST': 'red',
    'SEQUENCE': 'green',
    'HASH_MAP': 'blue',
    'TREE_MAP': 'yellow'
}
# Vectorize the mapping function
map_color = np.vectorize(color_map.get)

# Plot the DataFrame with colors based on class
# plt.scatter(df['Cross 1'], df['Cross 2'], c=map_color(df['Data Structure']))
plt.scatter(df["Cross 1"], df["Data Structure"])
plt.xlabel("Search Randomness")
plt.ylabel("Data Structure")
plt.show()