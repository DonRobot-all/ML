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

a = [ 0, 1, 0, 1]
b = [ 1, 0, 1, 0]
c = [ 0, 1, 1, 0]
d = [.5, 0,.5, 0]
e = [ 0, 1,-1, 0]

print(w_sum(a,b)) # = 0
print(w_sum(b,c)) # = 1
print(w_sum(b,d)) # = 1
print(w_sum(c,c)) # = 2
print(w_sum(d,d)) # = .5
print(w_sum(c,e)) # = 0