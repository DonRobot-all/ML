import tkinter as tk
import random
import torch
import torch.nn as nn

digits = torch.tensor([
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
], dtype=torch.float32)

targets = torch.arange(10)  # [0, 1, 2, ..., 9]

model     = nn.Sequential(nn.Linear(15, 20), nn.ReLU(), nn.Linear(20, 10))
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

for epoch in range(2000):
    optimizer.zero_grad()       # сбросить старые градиенты
    output = model(digits)      # прямой проход
    loss   = criterion(output, targets)  # считаем ошибку
    loss.backward()             # обратный проход — АВТОМАТИЧЕСКИ
    optimizer.step()            # обновить веса

    if epoch % 500 == 0:
        print("epoch:", epoch, "error:", round(loss.item(),3))

# ===== PREDICT =====

def predict(x):
    x = torch.tensor(x, dtype=torch.float32)

    output = model(x)

    print(output.tolist())  # посмотреть “уверенности”

    return torch.argmax(output).item()


# ===== GUI =====

root = tk.Tk()
root.title("Собери цифру 3x5 (PyTorch)")

grid = [[0 for _ in range(3)] for _ in range(5)]
buttons = []

def toggle(r, c):
    grid[r][c] = 1 - grid[r][c]
    color = "black" if grid[r][c] == 1 else "white"
    buttons[r][c].config(bg=color)


# создаём сетку
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


tk.Button(root, text="Показать массив", command=show_vector)\
    .grid(row=6, column=0, columnspan=3, sticky="we")

tk.Button(root, text="Распознать", command=recognize)\
    .grid(row=7, column=0, columnspan=3, sticky="we")

tk.Button(root, text="Очистить", command=clear)\
    .grid(row=8, column=0, columnspan=3, sticky="we")

label_vector = tk.Label(root, text="", font=("Arial", 10))
label_vector.grid(row=9, column=0, columnspan=3)

label_result = tk.Label(root, text="", font=("Arial", 16))
label_result.grid(row=10, column=0, columnspan=3)

root.mainloop()