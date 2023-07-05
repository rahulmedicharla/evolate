import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('machine_learning/data/visualization.csv')

df.plot(kind='scatter', x='Insertion/Deletion Frequency', y='Data Structure')
df.plot(kind='scatter', x='Search Randomness', y='Data Structure')

plt.show()