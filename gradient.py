price = 10
sales = 100

weight = 1
alpha = 0.01   # размер шага обучения

for i in range(100):

    pred = price * weight
    error = (pred - sales)

    gradient = price * error
    weight = weight - alpha * gradient

    print("step:", i, "weight:", round(weight,2))



weight =0.5
goal_pred =0.8
input =0.5
for iteration in range(20):
    pred = input * weight
    error = (pred - goal_pred) ** 2
    direction_and_amount = (pred - goal_pred) * input
    weight = weight - direction_and_amount
    print("Error:" + str(error) + " Prediction:" + str(pred))