prices = [5,6,7,8,9,10,11,12,13,14,
          15,16,17,18,19,20,21,22,23,24,
          25,26,27,28,29,30,31,32,33,34]

sales = [205,192,180,170,158,149,141,133,122,115,
         102,95,88,80,72,66,60,55,50,45,
         40,37,33,30,27,24,22,20,18,16]

# Параметры сети
num_neurons = 3           # количество нейронов
weights = [0.0]*num_neurons
biases = [0.0]*num_neurons

alpha = 0.0005           # скорость обучения
epochs = 2000

# Нейронная сеть: сумма нейронов
def neural_network(price, weights, biases):
    pred = 0
    for w, b in zip(weights, biases):
        pred += price * w + b   # линейный нейрон
    return pred

# Обучение
for epoch in range(epochs):
    total_error = 0
    for i in range(len(prices)):
        price = prices[i]
        target = sales[i]

        pred = neural_network(price, weights, biases)
        error = (pred - target)**2
        total_error += error

        # обновление каждого нейрона
        for j in range(num_neurons):
            gradient_w = (pred - target) * price
            gradient_b = (pred - target)

            weights[j] -= alpha * gradient_w
            biases[j]  -= alpha * gradient_b

    if epoch % 200 == 0:
        print(f"epoch: {epoch}, total_error: {round(total_error,2)}, weights: {[round(w,2) for w in weights]}, biases: {[round(b,2) for b in biases]}")

# Проверка модели
print("\nПроверка модели:")
for i in range(0, len(prices), 5):
    price = prices[i]
    pred = neural_network(price, weights, biases)
    print(f"price: {price}, real: {sales[i]}, pred: {round(pred,1)}")