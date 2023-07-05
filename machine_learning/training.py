import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('machine_learning/data/data.csv')

features = df[['Total Node Length', 'Insertion/Deletion Frequency', 'Search Randomness']]