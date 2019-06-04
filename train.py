import pandas as pd
import numpy as np
import seaborn as sns; sns.set()
import matplotlib.pyplot as plt
data = pd.read_csv('binary.csv', sep=',', dtype="int")



data1 = data[['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20', '21', '22', '23']] #Subsetting the data

print(data.describe())

cor = data1.corr() #Calculate the correlation of the above variables
sns.heatmap(cor, square = True) #Plot the correlation as heat map
plt.show()
# ax = sns.heatmap(data)
# plt.show()
