weights = [
    [ 1.2,  1.8,  0.9],   # вероятность победы
    [-0.6, -0.4, -0.2],  # tilt
    [ 0.3,  1.5,  0.4]   # мораль
]


data = [
    [2.1, 0.48, 420, 0],
    [3.4, 0.61, 510, 1],
    [1.8, 0.42, 380, 0],
    [4.2, 0.73, 560, 1]
]


# взвешенная сумма
def w_sum(a, b):
    assert(len(a) == len(b))
    out = 0
    for i in range(len(a)):
        out += a[i] * b[i]
    return out

# вектор * матрица
def vect_mat_mul(vect, matrix):
    assert(len(vect) == len(matrix))
    out = [0, 0, 0]
    for i in range(len(matrix)):
        out[i] = w_sum(vect, matrix[i])
    return out

def neural_network(input, weights):
    return vect_mat_mul(input, weights)

for row in data:
    KDA, WR, GPM, WIN = row
    input = [KDA/5, WR, GPM/600]
    pred = neural_network(input, weights)
    print(pred)
    print("Факт:", WIN,
          "Предсказание:", "WIN" if pred[0] > 2 else "LOSE")
