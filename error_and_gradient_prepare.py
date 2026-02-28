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
    ...

# вектор * матрица
def vect_mat_mul(vect, matrix):
    ...

def neural_network(input, weights):
    return vect_mat_mul(input, weights)

# === ОБУЧЕНИЕ МЕТОДОМ "ГОРЯЧО-ХОЛОДНО" ===
step_amount = 0.01  # размер шага
epochs = 100  # количество проходов по данным

for epoch in range(epochs):
    ...

print("\n=== РЕЗУЛЬТАТЫ ПОСЛЕ ОБУЧЕНИЯ ===\n")

for row in data:
    KDA, WR, GPM, WIN = row
    input_data = [KDA/5, WR, GPM/600]
    pred = neural_network(input_data, weights)
    goal = 2.5 if WIN else 1.5
    print(f"Предсказание: {pred[0]:.3f} (цель: {goal})")
    print(f"Факт: {'WIN' if WIN else 'LOSE'}, " +
          f"Предсказание: {'WIN' if pred[0] > 2 else 'LOSE'}\n")