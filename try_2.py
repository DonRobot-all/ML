# prices = [5,6,7,8,9,10,11,12,13,14,
# 15,16,17,18,19,20,21,22,23,24,
# 25,26,27,28,29,30,31,32,33,34]

# sales = [205,192,180,170,158,149,141,133,122,115,
# 102,95,88,80,72,66,60,55,50,45,
# 40,37,33,30,27,24,22,20,18,16]

# weight = 10
# alpha = 0.0001   # скорость обучения


# def neural_network(price, weight):
#     return price * weight


# def error(pred, target):
#     return (pred - target) ** 2


# for i in range(1000):

#     total_error = 0

#     for j in range(len(prices)):

#         price = prices[j]
#         target = sales[j]

#         # предсказание
#         pred = neural_network(price, weight)

#         # ошибка
#         e = pred - target
#         total_error += e**2

#         # градиент
#         gradient = e * price

#         # обновление веса
#         weight = weight - alpha * gradient

#     if i % 100 == 0:
#         print("итерация:", i, "ошибка:", total_error)


# print("обученный вес:", weight)


# print("\nПроверка модели:")

# for i in range(0, len(prices), 5):

#     price = prices[i]
#     pred = neural_network(price, weight)

#     print("price:", price,
#           "real:", sales[i],
#           "pred:", round(pred,1))

prices = [5,6,7,8,9,10,11,12,13,14,
15,16,17,18,19,20,21,22,23,24,
25,26,27,28,29,30,31,32,33,34]

sales = [205,192,180,170,158,149,141,133,122,115,
102,95,88,80,72,66,60,55,50,45,
40,37,33,30,27,24,22,20,18,16]

weight = 0.5  # начальный вес
epochs = 20   # количество итераций

def neural_network(price, weight):
    return price * weight

for epoch in range(epochs):

    total_error = 0

    for i in range(len(prices)):

        price = prices[i]
        target = sales[i]

        # предсказание
        pred = neural_network(price, weight)

        # ошибка
        error = (pred - target) ** 2
        total_error += error

        # градиентный шаг (direction_and_amount)
        direction_and_amount = (pred - target) * price

        # обновляем вес
        weight = weight - direction_and_amount

        print(f"Price: {price}, Error: {round(error,2)}, Prediction: {round(pred,2)}, Weight: {round(weight,2)}")

    print(f"--- Итог эпохи {epoch}, Средняя ошибка: {round(total_error/len(prices),2)} ---\n")

print("Обученный вес:", round(weight,2))

print("\nПроверка модели:")

for i in range(0, len(prices), 5):

    price = prices[i]
    pred = neural_network(price, weight)

    print("price:", price,
          "real:", sales[i],
          "pred:", round(pred,1))