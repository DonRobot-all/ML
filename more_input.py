# Данные: KDA, WR, GPM, WIN
data = [
    [2.1, 0.48, 420, 0],
    [3.4, 0.61, 510, 1],
    [1.8, 0.42, 380, 0],
    [4.2, 0.73, 560, 1]
]

# Инициализация весов
weights = [0.5, 0.5, 0.001]  # один вес для каждого входа
alpha = 0.01
epochs = 50

def neural_network(inputs, weights):
    pred = 0
    for i in range(len(inputs)):
        pred += inputs[i] * weights[i]
    return pred

for epoch in range(epochs):
    total_error = 0
    for row in data:
        inputs = [row[0]/5, row[1], row[2]/600]  # нормализация
        target = 2.5 if row[3]==1 else 1.5
        
        # предсказание
        pred = neural_network(inputs, weights)
        
        # ошибка
        error = (pred - target)**2
        total_error += error
        
        # обновление весов
        for i in range(len(weights)):
            gradient = (pred - target) * inputs[i]
            weights[i] = weights[i] - alpha * gradient
    
    if epoch % 10 == 0:
        print(f"Эпоха {epoch}, средняя ошибка: {total_error/len(data):.4f}")

print("Обученные веса:", weights)

# проверка модели
for row in data:
    inputs = [row[0]/5, row[1], row[2]/600]
    pred = neural_network(inputs, weights)
    goal = 2.5 if row[3]==1 else 1.5
    print(f"Pred: {pred:.2f}, Goal: {goal}")