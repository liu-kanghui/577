import pandas as pd
import numpy as np
import seaborn as sns; sns.set()
import matplotlib.pyplot as plt


from pandas.plotting import scatter_matrix
data = pd.read_csv('numeric.csv', sep=',', dtype="float")



data1 = data[
    ['church', 'resort', 'beach', 'park', 'theatre', 'museum', 'mall', 'zoo', 
                                    'restaurant', 'pub/bar', 'localservice', 'burger/pizza',
                                    'hotel', 'juicebar', 'artgallery', 'danceclub', 'swimmingpool', 
                                    'gym', 'bakery', 'beautyspa', 'cafe', 'viewpoint', 'monument', 
                                     'garden']
] #Subsetting the data

print(data.describe())

# data1.hist()

scatter_matrix(data1, alpha=0.2, figsize=(6, 6), diagonal='kde')
plt.show()

# plt.show()
