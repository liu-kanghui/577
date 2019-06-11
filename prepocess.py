
import pandas as pd
import numpy as np
data = pd.read_csv('google_review_ratings.csv', sep=',')
data_matrix = data.to_numpy()

# get rid of user and last column nam
data_matrix = data_matrix[:, 1:-1]

data_matrix = pd.DataFrame(data_matrix)

data_matrix.columns = ['church', 'resort', 'beach', 'park', 'theatre', 'museum', 'mall', 'zoo', 
                                    'restaurant', 'pub/bar', 'localservice', 'burger/pizza',
                                    'hotel', 'juicebar', 'artgallery', 'danceclub', 'swimmingpool', 
                                    'gym', 'bakery', 'beautyspa', 'cafe', 'viewpoint', 'monument', 
                                     'garden']

data_matrix.to_csv("numeric.csv")


# print(data_matrix[24])
# data_matrix.to_csv("numeric_ori.csv")
