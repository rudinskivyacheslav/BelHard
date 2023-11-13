#Вывести первые N цисел кратные M и больше K
number_of_numbers = int(input("Enter number of numbers: "))
divider = int(input("Enter divider: "))
initial_value = int(input("Enter initial value: "))

if divider:
    while number_of_numbers:
        initial_value += 1
        if not initial_value % divider:
            print(initial_value, end=" ")
            number_of_numbers -= 1
    else:
        print("Division by zero")
