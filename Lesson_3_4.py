#Пользователь вводит 3 числа, сказать сколько из них положительных и сколько отрицательных

value_1 = int(input("Enter value: "))
value_2 = int(input("Enter value: "))
value_3 = int(input("Enter value: "))

positive_values = (value_1 > 0) + (value_2 > 0) + (value_3 > 0)

print(f"Positive: {positive_values}")
print(f"Negative: {3-positive_values}")
