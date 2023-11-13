#**Вывести четные числа от 2 до N по 5 в строку
end_value = int(input("Enter end value: "))
start_value = 2
newline_counter = 0
while start_value <= end_value:
    if not start_value % 2:
        print(start_value, end=" ")
        newline_counter += 1
        if not newline_counter % 5:
            print()
    start_value += 1
