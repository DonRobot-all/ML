prices = [5,6,7,8,9,10,11,12,13,14,
15,16,17,18,19,20,21,22,23,24,
25,26,27,28,29,30,31,32,33,34]

sales = [205,192,180,170,158,149,141,133,122,115,
102,95,88,80,72,66,60,55,50,45,
40,37,33,30,27,24,22,20,18,16]

weight = 10
step = 0.01

def neural_network(price, weight):
    return price * weight

def error(pred, target):
    return (pred - target) ** 2

for i in range(1000):

    total_error = 0

    for j in range(len(prices)):

        price = prices[j]
        target = sales[j]

        pred = neural_network(price, weight)
        e = error(pred, target)

        pred_up = neural_network(price, weight + step)
        e_up = error(pred_up, target)

        pred_down = neural_network(price, weight - step)
        e_down = error(pred_down, target)

        if e_up < e:
            weight += step
        elif e_down < e:
            weight -= step

        total_error += e

    if i % 100 == 0:
        print("итерация:", i, "ошибка:", total_error)

print("обученный вес:", weight)


print("\nПроверка модели:")

for i in range(0, len(prices), 5):
    price = prices[i]
    pred = neural_network(price, weight)

    print("price:", price,
          "real:", sales[i],
          "pred:", round(pred,1))


# # данные
# prices = [5,6,7,8,9,10,11,12,13,14,
# 15,16,17,18,19,20,21,22,23,24,
# 25,26,27,28,29,30,31,32,33,34]

# sales = [205,192,180,170,158,149,141,133,122,115,
# 102,95,88,80,72,66,60,55,50,45,
# 40,37,33,30,27,24,22,20,18,16]


# # начальные параметры
# weight = -5
# bias = 200

# step = 5


# # нейрон
# def neural_network(price, weight, bias):
#     return price * weight + bias


# # ошибка
# def error(pred, target):
#     return (pred - target) ** 2


# # обучение
# for i in range(1000):

#     total_error = 0

#     for j in range(len(prices)):

#         price = prices[j]
#         target = sales[j]

#         pred = neural_network(price, weight, bias)
#         e = error(pred, target)

#         # проверяем изменение веса
#         pred_up = neural_network(price, weight + step, bias)
#         e_up = error(pred_up, target)

#         pred_down = neural_network(price, weight - step, bias)
#         e_down = error(pred_down, target)

#         if e_up < e:
#             weight += step
#         elif e_down < e:
#             weight -= step


#         # проверяем изменение bias
#         pred_up = neural_network(price, weight, bias + step)
#         e_up = error(pred_up, target)

#         pred_down = neural_network(price, weight, bias - step)
#         e_down = error(pred_down, target)

#         if e_up < e:
#             bias += step
#         elif e_down < e:
#             bias -= step


#         total_error += e


#     if i % 100 == 0:
#         print("итерация:", i, "ошибка:", total_error)


# print("\nОбученные параметры")
# print("weight:", weight)
# print("bias:", bias)


# # проверка
# print("\nПроверка модели")

# for i in range(0, len(prices), 5):

#     price = prices[i]
#     pred = neural_network(price, weight, bias)

#     print(
#         "price:", price,
#         "real:", sales[i],
#         "pred:", round(pred,1)
#     )