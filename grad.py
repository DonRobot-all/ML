def f(x):
    return (x - 3) ** 2

def grad(x):
    return 2 * (x - 3)   # производная f(x)

x = 0.0   # начальная точка
lr = 0.1  # скорость обучения

for i in range(20):
    g = grad(x)          # градиент — точный
    x = x - lr * g       # шаг вниз по склону
    print(f"шаг {i+1:2d}: x = {x:.4f}, f(x) = {f(x):.4f}")


# import random

# def f(x):
#     return (x - 3) ** 2

# def noisy_grad(x):
#     noise = random.uniform(-1.5, 1.5)  # шум — как один пример из датасета
#     return 2 * (x - 3) + noise

# x = 0.0
# lr = 0.1

# for i in range(20):
#     g = noisy_grad(x)    # градиент — шумный, по одному примеру
#     x = x - lr * g
#     print(f"шаг {i+1:2d}: x = {x:.4f}, f(x) = {f(x):.4f}")