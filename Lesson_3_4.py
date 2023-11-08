#Пользователь вводит 3 числа, сказать сколько из них положительных и сколько отрицательных

list_values = list(map( int, input("Enter values: "). split()))
positive_values = 0
for value in list_values:
    if value > 0:
        positive_values += 1
print(f"Positive: {positive_values}")
print(f"Negative: {len(list_values)-positive_values}")
