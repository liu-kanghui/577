
import pandas as pd
import numpy as np
data = pd.read_csv('google_review_ratings.csv', sep=',')
data_matrix = data.to_numpy()

data_matrix = data_matrix[:, 1:]

pd.DataFrame(data_matrix).to_csv("numeric.csv")
