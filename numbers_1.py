import tkinter as tk
import random

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
hidden_size = 20
output_size = 10

alpha = 0.01
epochs = 2000

# два шага обработки input → hidden → output
w1 = [[random.uniform(-0.1,0.1) for _ in range(input_size)] for _ in range(hidden_size)]
b1 = [0 for _ in range(hidden_size)]

w2 = [[random.uniform(-0.1,0.1) for _ in range(hidden_size)] for _ in range(output_size)]
b2 = [0 for _ in range(output_size)]


def w_sum(a, b):
    out = 0
    for i in range(len(a)):
        out += a[i] * b[i]
    return out


"""
если у нас 3 входа [1, 0, 1] и нейрон имеет веса [0.5, -0.2, 0.3] и смещение 0.1
То: (1*0.5 + 0*(-0.2) + 1*0.3) + 0.1 = 0.5 + 0 + 0.3 + 0.1 = 0.9
"""
def layer(inputs, weights, bias):
    out = []
    for i in range(len(weights)):
        out.append(w_sum(inputs, weights[i]) + bias[i])
    return out

"""
Rectified Linear Unit  (выпрямленная линейная единица)
Вносит нелинейность - если бы все функции были линейными, сеть не могла бы обучаться сложным закономерностям
"""
def relu(x):
    return [max(0, i) for i in x]


def neural_network(x):
    hidden = layer(x, w1, b1)
    hidden = relu(hidden)

    output = layer(hidden, w2, b2)

    return hidden, output


for epoch in range(epochs):

    total_error = 0

    for digit in range(10):

        x = digits[digit]

        target = [0]*10
        target[digit] = 1

        hidden, output = neural_network(x)

        # ошибка
        errors = []
        for i in range(10):
            e = output[i] - target[i]
            errors.append(e)
            total_error += e*e

        # ===== ОБУЧАЕМ ВТОРОЙ СЛОЙ =====
        for i in range(output_size):   # 10
            for j in range(hidden_size):
                w2[i][j] -= alpha * errors[i] * hidden[j]
            b2[i] -= alpha * errors[i]

        # ===== ОШИБКА СКРЫТОГО СЛОЯ =====
        hidden_errors = [0]*hidden_size

        for j in range(hidden_size):
            for i in range(output_size):
                hidden_errors[j] += errors[i] * w2[i][j]

        for j in range(hidden_size):
            if hidden[j] == 0:
                hidden_errors[j] = 0

        # ===== ОБУЧАЕМ ПЕРВЫЙ СЛОЙ =====
        for j in range(hidden_size):
            for k in range(input_size):
                w1[j][k] -= alpha * hidden_errors[j] * x[k]
            b1[j] -= alpha * hidden_errors[j]

    if epoch % 500 == 0:
        print("epoch:", epoch, "error:", round(total_error,3))


# Выбираем максимальный
def predict(x):
    _, output = neural_network(x)
    print(output)
    return output.index(max(output))


# ===== GUI =====

root = tk.Tk()
root.title("Собери цифру 3x5")

grid = [[0 for _ in range(3)] for _ in range(5)]
buttons = []

def toggle(r, c):
    grid[r][c] = 1 - grid[r][c]  # переключение 0/1
    color = "black" if grid[r][c] == 1 else "white"
    buttons[r][c].config(bg=color)


for r in range(5):
    row = []
    for c in range(3):
        btn = tk.Button(root, width=6, height=3,
                        bg="white",
                        command=lambda r=r, c=c: toggle(r, c))
        btn.grid(row=r, column=c)
        row.append(btn)
    buttons.append(row)


def build_vector():
    flat = []
    for r in range(5):
        for c in range(3):
            flat.append(grid[r][c])
    return flat


def show_vector():
    vec = build_vector()
    label_vector.config(text=str(vec))


def recognize():
    vec = build_vector()
    pred = predict(vec)
    label_result.config(text=f"Это: {pred}")


def clear():
    for r in range(5):
        for c in range(3):
            grid[r][c] = 0
            buttons[r][c].config(bg="white")
    label_vector.config(text="")
    label_result.config(text="")


tk.Button(root, text="Показать массив", command=show_vector).grid(row=6, column=0, columnspan=3, sticky="we")
tk.Button(root, text="Распознать", command=recognize).grid(row=7, column=0, columnspan=3, sticky="we")
tk.Button(root, text="Очистить", command=clear).grid(row=8, column=0, columnspan=3, sticky="we")

label_vector = tk.Label(root, text="", font=("Arial", 10))
label_vector.grid(row=9, column=0, columnspan=3)

label_result = tk.Label(root, text="", font=("Arial", 16))
label_result.grid(row=10, column=0, columnspan=3)

root.mainloop()