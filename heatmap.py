import pandas as pd
import numpy as np
import seaborn as sns; sns.set()
import matplotlib.pyplot as plt
data = pd.read_csv('numeric.csv', sep=',', dtype="float")



data1 = data[
        ['church', 'resort', 'beach', 'park', 'theatre', 'museum', 'mall', 'zoo', 
                                    'restaurant', 'pub/bar', 'localservice', 'burger/pizza',
                                    'hotel', 'juicebar', 'artgallery', 'danceclub', 'swimmingpool', 
                                    'gym', 'bakery', 'beautyspa', 'cafe', 'viewpoint', 'monument', 
                                     'garden']
] 

print(data.describe())

cor = data1.corr() #Calculate the correlation of the above variables
sns.heatmap(cor, square = True) #Plot the correlation as heat map
plt.show()
