# def w_sum(a,b):
#     result = 0
#     for i in range(len(a)):
#         result += (a[i] * b[i])
#     return result
# weights = [0.1, 0.2, 0]
# def neural_network(data, weights):
#     pred = w_sum(data,weights)
#     return pred
# toes = [8.5, 9.5, 9.9, 9.0]
# wlrec = [0.65, 0.8, 0.8, 0.9]
# nfans = [1.2, 1.3, 0.5, 1.0]
# data = [toes[0],wlrec[0],nfans[0]]
# pred = neural_network(data,weights)
# print(pred)

import numpy as np
weights = np.array([0.1, 0.2, 0])
def neural_network(data, weights):
    pred = data.dot(weights)
    return pred
toes = np.array([8.5, 9.5, 9.9, 9.0])
wlrec = np.array([0.65, 0.8, 0.8, 0.9])
nfans = np.array([1.2, 1.3, 0.5, 1.0])
data = np.array([toes[0],wlrec[0],nfans[0]])
pred = neural_network(data,weights)
print(pred)

# import numpy as np

# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])
# out = np.empty(())  # Скалярный контейнер

# # Медленно (создаёт новый объект)
# result1 = np.dot(a, b)  # 32

# # Быстро (использует out)
# np.dot(a, b, out=out)
# print(out)  # 32
