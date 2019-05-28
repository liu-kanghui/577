
import pandas as pd
import numpy as np
data = pd.read_csv('google_review_ratings.csv', sep=',')
data_matrix = data.to_numpy()
# print(data_matrix[0])

data_matrix = data_matrix[:, 1:]


pd.DataFrame(data_matrix).to_csv("matrix.csv")

print(data_matrix[:, 0])
# np.savetxt('matrixdata.csv', data_matrix, delimiter=",")

# data_matrix = pd.to_numeric(data_matrix)

# data_matrix[data_matrix > 2.5] = 1
# data_matrix[data_matrixdata <= 2.5] = 0
# print(data_matrix)
# print(data_matrix.shape)


# Plot the data

#User,Category 1,Category 2,Category 3,Category 4,Category 5,
#Category 6,Category 7,Category 8,Category 9,Category 10,Category 11,
# Category 12,Category 13,Category 14,Category 15,Category 16,Category 17,
# Category 18,Category 19,Category 20,Category 21,Category 22,Category 23,Category 24,
# plt.scatter(data['Category8'], data['Category9'], s=0.2)
# plt.axis('equal')
# plt.axis('off')
# plt.xticks([])
# plt.yticks([])
# plt.show()