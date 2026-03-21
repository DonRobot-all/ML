weights = [
    [1.2, 1.8, 0.9],   # вероятность победы
    [-0.6, -0.4, -0.2],
    [0.3, 1.5, 0.4]
]

data = [
    [2.1, 0.48, 420, 0],
    [3.4, 0.61, 510, 1],
    [1.8, 0.42, 380, 0],
    [4.2, 0.73, 560, 1]
]


def w_sum(a, b):
    assert(len(a) == len(b))
    out = 0
    for i in range(len(a)):
        out += a[i] * b[i]
    return out


def vect_mat_mul(vect, matrix):
    assert(len(vect) == len(matrix))
    out = [0, 0, 0]
    for i in range(len(matrix)):
        out[i] = w_sum(vect, matrix[i])
    return out


def neural_network(input, weights):
    return vect_mat_mul(input, weights)


# === ОБУЧЕНИЕ ГРАДИЕНТНЫМ СПУСКОМ ===

alpha = 0.1   # скорость обучения
epochs = 100

for epoch in range(epochs):

    total_error = 0

    for row in data:

        KDA, WR, GPM, WIN = row
        input_data = [KDA/5, WR, GPM/600]

        pred = neural_network(input_data, weights)
        goal = 2.5 if WIN else 1.5

        error = (pred[0] - goal)
        total_error += error ** 2

        # обновляем веса первого нейрона
        for i in range(3):

            gradient = error * input_data[i]

            weights[0][i] = weights[0][i] - alpha * gradient


    if epoch % 20 == 0:
        print(f"Эпоха {epoch}, Средняя ошибка: {total_error/len(data):.4f}")


print("\n=== РЕЗУЛЬТАТЫ ПОСЛЕ ОБУЧЕНИЯ ===\n")

for row in data:

    KDA, WR, GPM, WIN = row
    input_data = [KDA/5, WR, GPM/600]

    pred = neural_network(input_data, weights)
    goal = 2.5 if WIN else 1.5

    print(f"Предсказание: {pred[0]:.3f} (цель: {goal})")
    print(f"Факт: {'WIN' if WIN else 'LOSE'}, "
          f"Предсказание: {'WIN' if pred[0] > 2 else 'LOSE'}\n")