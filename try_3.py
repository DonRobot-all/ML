prices = [5,6,7,8,9,10,11,12,13,14,
15,16,17,18,19,20,21,22,23,24,
25,26,27,28,29,30,31,32,33,34]

sales = [205,192,180,170,158,149,141,133,122,115,
102,95,88,80,72,66,60,55,50,45,
40,37,33,30,27,24,22,20,18,16]

weight = 0
bias = 0

alpha = 0.001
epochs = 2000


def neural_network(price, weight, bias):
    return price * weight + bias


for epoch in range(epochs):

    total_error = 0

    for i in range(len(prices)):

        price = prices[i]
        target = sales[i]

        # предсказание
        pred = neural_network(price, weight, bias)

        # ошибка
        error = (pred - target) ** 2
        total_error += error

        # градиенты
        gradient_w = (pred - target) * price
        gradient_b = (pred - target)

        # обновление параметров
        weight = weight - alpha * gradient_w
        bias = bias - alpha * gradient_b

    if epoch % 20 == 0:
        print("epoch:", epoch,
              "error:", round(total_error,2),
              "weight:", round(weight,3),
              "bias:", round(bias,3))


print("\nОбученные параметры:")
print("weight:", round(weight,3))
print("bias:", round(bias,3))


print("\nПроверка модели:")

for i in range(0, len(prices), 5):

    price = prices[i]
    pred = neural_network(price, weight, bias)

    print(
        "price:", price,
        "real:", sales[i],
        "pred:", round(pred,1)
    )