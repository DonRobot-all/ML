import numpy as np

weights = np.array([0.5, 0.48, -0.7])
alpha = 0.1

streetlights = np.array([
    [1,0,1],
    [0,1,1],
    [0,0,1],
    [1,1,1],
    [0,1,1],
    [1,0,1],
])

walk_vs_stop = np.array([0,1,0,1,1,0])

epochs = 50

for epoch in range(epochs):

    total_error = 0

    for iteration in range(len(streetlights)):

        input = streetlights[iteration]
        target = walk_vs_stop[iteration]

        # предсказание
        prediction = input.dot(weights)

        # ошибка
        error = (prediction - target) ** 2
        total_error += error

        # градиент
        gradient = (prediction - target) * input

        # обновление весов
        weights = weights - alpha * gradient

    if epoch % 10 == 0:
        print("epoch:", epoch, "error:", round(total_error,3))


print("\nОбученные веса:")
print(weights)


print("\nПроверка модели:")

for i in range(len(streetlights)):

    input = streetlights[i]
    pred = input.dot(weights)

    print(
        "input:", input,
        "pred:", round(pred,3),
        "target:", walk_vs_stop[i]
    )

# import numpy as np

# weights = np.array([0.5,0.48,-0.7])
# alpha = 0.1
# streetlights = np.array( [ 
#         [ 1, 0, 1 ],
#         [ 0, 1, 1 ],
#         [ 0, 0, 1 ],
#         [ 1, 1, 1 ],
#         [ 0, 1, 1 ],
#         [ 1, 0, 1 ], 
#         ] )
# walk_vs_stop = np.array( [ 0, 1, 0, 1, 1, 0 ] )

# input = streetlights [0] #◄------ [1,0,1]
# target = walk_vs_stop[0] #◄------ Содержит 0 (стоять)
# epochs = 500
# for epoch in range(epochs):
#     for iteration in range(6):
#         input = streetlights [iteration] #◄------ [1,0,1]
#         target = walk_vs_stop[iteration] #◄------ Содержит 0 (стоять)
#         prediction = input.dot(weights)
#         error = (target - prediction) ** 2
#         gradient = (prediction - target) * input
#         weights = weights - (alpha * (input * gradient))
#         print("Error:" + str(error) + " Prediction:" + str(prediction))


# print("\nОбученные параметры:")
# print("weight:", weights)
# print("bias:", weights)


# print("\nПроверка модели:")

# for i in range(0, len(streetlights)):

#     input = streetlights[i]
#     pred = input.dot(weights)

#     print(
#         "price:", input,
#         # "real:", sales[i],
#         "pred:", round(pred,1)
#     )