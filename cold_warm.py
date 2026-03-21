# weight = 0.5
# input = 0.5
# goal_prediction = 0.8 
# step_amount = 0.001 
# for iteration in range(1101): 
#     prediction = input * weight
#     error = (prediction - goal_prediction) ** 2
#     print("Error:" + str(error) + " Prediction:" + str(prediction))
#     up_prediction = input * (weight + step_amount) # ◄------ Попробовать увеличить!
#     up_error = (goal_prediction - up_prediction) ** 2
#     down_prediction = input * (weight - step_amount) # ◄------ Попробовать уменьшить!
#     down_error = (goal_prediction - down_prediction) ** 2
#     if(down_error < up_error):
#         weight = weight - step_amount #◄-------- , Еckи уменьшение дало лучший результат
#     if(down_error > up_error):
#         weight = weight + step_amount 


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

# взвешенная сумма
def w_sum(a, b):
    assert(len(a) == len(b))
    out = 0
    for i in range(len(a)):
        out += a[i] * b[i]
    return out

# вектор * матрица
def vect_mat_mul(vect, matrix):
    assert(len(vect) == len(matrix))
    out = [0, 0, 0]
    for i in range(len(matrix)):
        out[i] = w_sum(vect, matrix[i])
    return out

def neural_network(input, weights):
    return vect_mat_mul(input, weights)

# === ОБУЧЕНИЕ МЕТОДОМ "ГОРЯЧО-ХОЛОДНО" ===
step_amount = 0.01  # размер шага
epochs = 100  # количество проходов по данным

for epoch in range(epochs):
    total_error = 0
    
    for row in data:
        KDA, WR, GPM, WIN = row
        input_data = [KDA/5, WR, GPM/600]
        
        # Текущее предсказание
        pred = neural_network(input_data, weights)
        goal = 2.5 if WIN == 1 else 1.5  # цель: 2.5 для победы, 1.5 для поражения
        current_error = (pred[0] - goal) ** 2
        total_error += current_error
        
        # Пробуем изменить каждый вес первого нейрона
        for i in range(3):  # для каждого веса в первом нейроне
            # Пробуем увеличить вес
            weights[0][i] += step_amount
            pred_up = neural_network(input_data, weights)[0]
            up_error = (pred_up - goal) ** 2
            
            # Пробуем уменьшить вес
            weights[0][i] -= 2 * step_amount  # отнимаем шаг (был +, стал -)
            pred_down = neural_network(input_data, weights)[0]
            down_error = (pred_down - goal) ** 2
            
            # Возвращаем вес на место
            weights[0][i] += step_amount
            
            # Выбираем направление с меньшей ошибкой
            if down_error < up_error and down_error < current_error:
                weights[0][i] -= step_amount  # уменьшаем
            elif up_error < down_error and up_error < current_error:
                weights[0][i] += step_amount  # увеличиваем
    
    if epoch % 20 == 0:
        print(f"Эпоха {epoch}, Средняя ошибка: {total_error/len(data):.4f}")

print("\n=== РЕЗУЛЬТАТЫ ПОСЛЕ ОБУЧЕНИЯ ===\n")

for row in data:
    KDA, WR, GPM, WIN = row
    input_data = [KDA/5, WR, GPM/600]
    pred = neural_network(input_data, weights)
    goal = 2.5 if WIN else 1.5
    print(f"Предсказание: {pred[0]:.3f} (цель: {goal})")
    print(f"Факт: {'WIN' if WIN else 'LOSE'}, " +
          f"Предсказание: {'WIN' if pred[0] > 2 else 'LOSE'}\n")