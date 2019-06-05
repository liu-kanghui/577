import numpy as np
from sklearn.decomposition import ProjectedGradientNMF
import pandas as pd

data = pd.read_csv('binary.csv', sep=',', dtype="int")

X = data.to_numpy()

model = ProjectedGradientNMF(n_components=24, init='random',
                             random_state=0)