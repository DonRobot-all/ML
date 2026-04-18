import random

# ===== ДАННЫЕ =====

digits = [
[1,1,1, 1,0,1, 1,0,1, 1,0,1, 1,1,1],  # 0
[0,1,0, 1,1,0, 0,1,0, 0,1,0, 1,1,1],  # 1
[1,1,1, 0,0,1, 1,1,1, 1,0,0, 1,1,1],  # 2
[1,1,1, 0,0,1, 1,1,1, 0,0,1, 1,1,1],  # 3
[1,0,1, 1,0,1, 1,1,1, 0,0,1, 0,0,1],  # 4
[1,1,1, 1,0,0, 1,1,1, 0,0,1, 1,1,1],  # 5
[1,1,1, 1,0,0, 1,1,1, 1,0,1, 1,1,1],  # 6
[1,1,1, 0,0,1, 0,0,1, 0,0,1, 0,0,1],  # 7
[1,1,1, 1,0,1, 1,1,1, 1,0,1, 1,1,1],  # 8
[1,1,1, 1,0,1, 1,1,1, 0,0,1, 1,1,1],  # 9
]

input_size = 15
output_size = 10

# веса около 0 (не только положительные)
weights = [[random.uniform(-0.1, 0.1) for _ in range(input_size)] for _ in range(output_size)]
bias = [0.0] * output_size

alpha = 0.01
epochs = 2000


def w_sum(a, b):
    out = 0
    for i in range(len(a)):
        out += a[i] * b[i]
    return out


def neural_network(input, weights, bias):
    out = []
    for i in range(len(weights)):
        out.append(w_sum(input, weights[i]) + bias[i])
    return out


# ===== ОБУЧЕНИЕ =====

for epoch in range(epochs):  # ЭПОХИ

    total_error = 0

    for digit_index in range(10): # ВСЕ ЦИФРЫ

        input_data = digits[digit_index]

        target = [0]*10
        target[digit_index] = 1

        pred = neural_network(input_data, weights, bias)

        for n in range(output_size): # ВСЕ НЕЙРОНЫ

            error = pred[n] - target[n]
            total_error += error**2

            for i in range(input_size): # ВСЕ ВЕСА
                weights[n][i] -= alpha * error * input_data[i]

            # добавили bias
            bias[n] -= alpha * error

    if epoch % 200 == 0:
        print("epoch:", epoch, "error:", round(total_error,3))


# ===== ПРОВЕРКА =====

print("\nПРОВЕРКА")
for d in range(10):
    pred = neural_network(digits[d], weights, bias)
    guess = pred.index(max(pred))
    print("digit:", d, "prediction:", guess)


# ===== GUI =====

import tkinter as tk
from PIL import Image, ImageDraw
import numpy as np


def predict(input_data):
    preds = []
    for i in range(len(weights)):
        preds.append(np.dot(input_data, weights[i]) + bias[i])
    return preds.index(max(preds))


canvas_size = 100

root = tk.Tk()
root.title("Нарисуй цифру")

canvas = tk.Canvas(root, width=canvas_size, height=canvas_size, bg="white")
canvas.pack()

image = Image.new("L", (canvas_size, canvas_size), 255)
draw = ImageDraw.Draw(image)


def paint(event):
    x1, y1 = (event.x - 5), (event.y - 5)
    x2, y2 = (event.x + 5), (event.y + 5)
    canvas.create_oval(x1, y1, x2, y2, fill="black")
    draw.ellipse([x1, y1, x2, y2], fill=0)


canvas.bind("<B1-Motion>", paint)


def clear():
    canvas.delete("all")
    draw.rectangle([0, 0, canvas_size, canvas_size], fill=255)
    label.config(text="")


def recognize():
    small = image.resize((3,5))
    data = np.array(small)

    input_data = (data < 128).astype(int).flatten()

    pred = predict(input_data)

    label.config(text=f"Это: {pred}")


tk.Button(root, text="Распознать", command=recognize).pack()
tk.Button(root, text="Очистить", command=clear).pack()

label = tk.Label(root, text="", font=("Arial", 20))
label.pack()

root.mainloop()