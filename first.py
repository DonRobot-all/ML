# weight = 0.1

# def neural_network(data, weight):
#     prediction = data * weight
#     return prediction

# numbers = [8.5, 9.5, 10, 9]
# data = numbers[0]
# pred = neural_network(data, weight)
# print(pred)

def w_sum(a,b):
    result = 0
    for i in range(len(a)):
        result += (a[i] * b[i])
    return result

weight = [0.1, 0.2, 0]
def neural_network(data, weight):
    prediction = w_sum(data, weight)
    return prediction

toes = [8.5, 9.5, 9.9, 9.0]
wlrec = [0.65, 0.8, 0.8, 0.9]
nfans = [1.2, 1.3, 0.5, 1.0]
data = [toes[0], wlrec[0], nfans[0]]
pred = neural_network(data, weight)
print(pred)
