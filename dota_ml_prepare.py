weights = [
    [ 1.2,  1.8,  0.9],   # вероятность победы
    [-0.6, -0.4, -0.2],  # tilt
    [ 0.3,  1.5,  0.4]   # мораль
]


data = [
    [2.1, 0.48, 420, 0],
    [3.4, 0.61, 510, 1],
    [1.8, 0.42, 380, 0],
    [4.2, 0.73, 560, 1]
]


for row in data:
    KDA, WR, GPM, WIN = row
    input = [KDA/5, WR, GPM/600]
    pred = neural_network(input, weights)
    print(pred)
    print("Факт:", WIN,
          "Предсказание:", "WIN" if pred[0] > 2 else "LOSE")
