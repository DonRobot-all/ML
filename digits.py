digits = [

# 0
[1,1,1,
 1,0,1,
 1,0,1,
 1,0,1,
 1,1,1],

# 1
[0,1,0,
 1,1,0,
 0,1,0,
 0,1,0,
 1,1,1],

# 2
[1,1,1,
 0,0,1,
 1,1,1,
 1,0,0,
 1,1,1],

# 3
[1,1,1,
 0,0,1,
 1,1,1,
 0,0,1,
 1,1,1],

# 4
[1,0,1,
 1,0,1,
 1,1,1,
 0,0,1,
 0,0,1],

# 5
[1,1,1,
 1,0,0,
 1,1,1,
 0,0,1,
 1,1,1],

# 6
[1,1,1,
 1,0,0,
 1,1,1,
 1,0,1,
 1,1,1],

# 7
[1,1,1,
 0,0,1,
 0,0,1,
 0,0,1,
 0,0,1],

# 8
[1,1,1,
 1,0,1,
 1,1,1,
 1,0,1,
 1,1,1],

# 9
[1,1,1,
 1,0,1,
 1,1,1,
 0,0,1,
 1,1,1]

]

import random

# количество входов
input_size = 15

# количество нейронов (10 цифр)
output_size = 10

# веса 10×15
weights = [[random.random()*0.1 for i in range(input_size)] for j in range(output_size)]

alpha = 0.01


def w_sum(a,b):
    out = 0
    for i in range(len(a)):
        out += a[i]*b[i]
    return out


def neural_network(input, weights):

    out = []

    for neuron_weights in weights:
        out.append(w_sum(input, neuron_weights))

    return out


# обучение
for epoch in range(200):

    total_error = 0

    for digit_index in range(10):

        input = digits[digit_index]

        target = [0]*10
        target[digit_index] = 1

        pred = neural_network(input, weights)

        for n in range(output_size):

            error = pred[n] - target[n]
            total_error += error**2

            for i in range(input_size):

                weights[n][i] -= alpha * error * input[i]

    if epoch % 20 == 0:
        print("epoch:", epoch, "error:", round(total_error,3))


print("\nПРОВЕРКА")

for d in range(10):

    pred = neural_network(digits[d], weights)

    guess = pred.index(max(pred))

    print("digit:", d, "prediction:", guess)