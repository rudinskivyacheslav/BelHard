#Пользователь вводит Имя, Возраст и Город, сформировать приветственное сообщение путем форматирования 3-мя способами

name = input("Enter name: ")
age = int(input("Enter age: "))
city = input("Enter city: ")
print(f"Name: {name}\t Age: {age}\t City: {city}")
print("Name: {}\t Age: {}\t City: {}".format(name, age, city))
print("Name: %s\t Age: %s\t City: %s" % (name, age, city))
