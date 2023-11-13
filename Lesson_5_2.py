#Сделать калькулятор: у пользователя спрашивается число, потом действие и второе число
first_value = int(input("Enter first value: "))
action = input("Enter action: ")
second_value = int(input("Enter second value: "))
print(f"{first_value} {action} {second_value} = ", end="")

match action:
    case "+":
        print(first_value + second_value)
    case "-":
        print(first_value - second_value)
    case "*":
        print(first_value * second_value)
    case "/":
        if second_value:
            print(first_value / second_value)
        else:
            print("Division by zero")
    case _:
        print("Wrong action")
