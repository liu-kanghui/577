import pandas as pd
import numpy as np
import seaborn as sns; sns.set()
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
from sklearn.neighbors import NearestNeighbors
from sklearn.model_selection import train_test_split
import copy

data = pd.read_csv('numeric.csv',sep=',', dtype="float")

binary_data = pd.read_csv('new_binary.csv',sep=',')

# get rid of first column nan value
data = data.to_numpy()[:, 1:]
binary_data = binary_data.to_numpy()[:, 1:]
# replace NAN to 0
data = np.nan_to_num(data)

list_places = ['church', 'resort', 'beach', 'park', 'theatre', 'museum', 'mall', 'zoo', 
                                    'restaurant', 'pub/bar', 'localservice', 'burger/pizza',
                                    'hotel', 'juicebar', 'artgallery', 'danceclub', 'swimmingpool', 
                                    'gym', 'bakery', 'beautyspa', 'cafe', 'viewpoint', 'monument', 
                                     'garden']

indices = np.arange(len(data))
X_train, X_test, train_indices, test_indices = train_test_split(binary_data, indices, test_size=0.33, random_state=0)

# the training should exclude the number 
feature_used = [ 11, 12, 13, 14, 15, 16, 17]

# num_recommend
num_recommend = 5

# deep copy X_test 
all_feature_X_test = copy.deepcopy(X_test)

# print out the ground truth of recommended place. 
ground_truth_list = []
for instance in all_feature_X_test:
    ground_truth =  np.flip(np.argsort(instance)).tolist()

    # remove selected features
    for item in feature_used:
        if item in ground_truth:
            ground_truth.remove(item)

    # only choose  num_recommend recommendations
    recommend = []
    while( len(ground_truth) != 0 and len(recommend) < num_recommend):
        recommend.append(ground_truth.pop())
    
    # add to a list of list
    # convert to set, easy for calculate the accuracy
    # print (recommend)
    ground_truth_list.append(set(recommend))

    # convert index to category name
    places = []
    for item in recommend:
        places.append(list_places[item])
    # print (places)

# use only selected known feature to train
X_train = X_train[:, feature_used]
X_test = X_test[:, feature_used]

# only used the nearest neighbor
model_knn = NearestNeighbors( algorithm='brute', n_neighbors= 20, n_jobs=-1).fit(X_train)
distances, indices = model_knn.kneighbors(X_test, n_neighbors = 1)


print('Recommendations:')

predict_list = []
for eachOne in indices:

    predict = np.flip(np.argsort(data[eachOne[0]])).tolist()

    for item in feature_used:
        if item in predict:
            predict.remove(item)
    recommend = []
    while( len(predict) != 0 and len(recommend) < num_recommend):
        recommend.append(predict.pop())

    # convert to set, easy for calculate the accuracy
    # print (recommend)
    predict_list.append(set(recommend))

    places = []
    for place in recommend:
        places.append(list_places[place])
    # print (places)

same_count = 0
total_element = 0
for index, each_list in enumerate(predict_list):
    for item in each_list:
        if item in ground_truth_list[index]:
            same_count += 1
        total_element += 1

print ("{0:.0%}".format(same_count / total_element))
print (same_count / total_element )