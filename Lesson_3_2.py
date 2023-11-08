#Пользователь вводит 3 числа, найти среднее арифмитическое с точность 3

value1 = int(input("Enter value1: "))
value2 = int(input("Enter value2: "))
value3 = int(input("Enter value3: "))
sum_values = value1 + value2 + value3
result = round(sum_values / 3, 1)
print(f"Average: {result}")
