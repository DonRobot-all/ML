import matplotlib.pyplot as plt
import numpy as np

# Данные
prices = np.array([5,10,15,20,25,30])
sales  = np.array([200,150,100,60,40,20])

# Вход для сети
x = prices

# Нейрон без bias
w = -5
b0 = 0
y_no_bias = w * x + b0

# Нейрон с bias
b = 220
y_with_bias = w * x + b

# График
plt.scatter(prices, sales, color='black', label='реальные продажи')
plt.plot(x, y_no_bias, 'r--', label='нейрон без bias')
plt.plot(x, y_with_bias, 'b-', label='нейрон с bias')
plt.xlabel("Цена")
plt.ylabel("Продажи")
plt.title("Зачем нужен bias в нейроне")
plt.legend()
plt.show()