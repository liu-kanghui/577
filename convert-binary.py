import pandas as pd
import numpy as np
data = pd.read_csv('numeric.csv', sep=',', dtype="float")

# convert all rating to binary 
# if a score > 2.5 than you get 1, if less than 2.5, you get a 0
# so 24 categories.
data['0'] = (data['0'] > 2.5).astype(int)
data['1'] = (data['1'] > 2.5).astype(int)
data['2'] = (data['2'] > 2.5).astype(int)
data['3'] = (data['3'] > 2.5).astype(int)
data['4'] = (data['4'] > 2.5).astype(int)
data['5'] = (data['5'] > 2.5).astype(int)
data['6'] = (data['6'] > 2.5).astype(int)
data['7'] = (data['7'] > 2.5).astype(int)
data['8'] = (data['8'] > 2.5).astype(int)
data['9'] = (data['9'] > 2.5).astype(int)
data['10'] = (data['10'] > 2.5).astype(int)
data['11'] = (data['11'] > 2.5).astype(int)
data['12'] = (data['12'] > 2.5).astype(int)
data['13'] = (data['13'] > 2.5).astype(int)
data['14'] = (data['14'] > 2.5).astype(int)
data['15'] = (data['15'] > 2.5).astype(int)
data['16'] = (data['16'] > 2.5).astype(int)
data['17'] = (data['17'] > 2.5).astype(int)
data['18'] = (data['18'] > 2.5).astype(int)
data['19'] = (data['19'] > 2.5).astype(int)
data['20'] = (data['20'] > 2.5).astype(int)
data['21'] = (data['21'] > 2.5).astype(int)
data['22'] = (data['22'] > 2.5).astype(int)
data['23'] = (data['23'] > 2.5).astype(int)

# get rid of first column 'user' and last column 'NaN'
data_matrix = data.to_numpy()
data_matrix = data_matrix[: , 1:-1]

pd.DataFrame(data_matrix).to_csv("binary.csv")

# till this points everything work like a magic! 
print(data_matrix)
print(data_matrix.shape)