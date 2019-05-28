import pandas as pd
import numpy as np
data = pd.read_csv('matrix.csv', sep=',', dtype="float")
data_matrix = data.to_numpy()

# get rid of first column user and last column 'NaN'

data_matrix = data_matrix[: , 1:-1]

# till this points everything work like a magic! 
print(data_matrix)
print(data_matrix.shape)