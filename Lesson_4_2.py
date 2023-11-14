#Без использования collections, написать программу, которая будет создавать словарь для
# подсчитывания количества вхождений каждой буквы в текст введенный с клавиатуры

text = input("Enter text: ")

dic = {i: text.count((i)) for i in set(text) if i.isalpha()}

for i in dic:
    print(f"{i}: {dic[i]}")
