#*Заполнить словарь где ключами будут выступать числа от 0 до n, а значениями вложенный словарь
# с ключами "name" и "email", а значения для этих ключей будут браться с клавиатуры

n = int(input("Enter n: "))
lst = ["name", "email"]
dic = {i: {j: (input(f"Enter {j}: ")) for j in lst} for i in range(n+1)}

print(dic)
