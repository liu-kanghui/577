import pandas as pd
import numpy as np
data = pd.read_csv('numeric.csv')

# convert all rating to binary 
# if a score > 2.5 than you get 1, if less than 2.5, you get a 0
# so 24 categories.

list_places = ['church', 'resort', 'beach', 'park', 'theatre', 'museum', 'mall', 'zoo', 
                                    'restaurant', 'pub/bar', 'localservice', 'burger/pizza',
                                    'hotel', 'juicebar', 'artgallery', 'danceclub', 'swimmingpool', 
                                    'gym', 'bakery', 'beautyspa', 'cafe', 'viewpoint', 'monument', 
                                     'garden']
for item in list_places:
    data[item] = (data[item] > 2.5).astype(int)


# get rid of the first row info 
data = pd.DataFrame(data.to_numpy()[:, 1:])

data.columns =  list_places
data.to_csv("new_binary.csv")

# till this points everything work like a magic! 
print(data.shape)