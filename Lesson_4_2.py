#Без использования collections, написать программу, которая будет создавать словарь для
# подсчитывания количества вхождений каждой буквы в текст введенный с клавиатуры

text = input("Enter text: ").replace(" ", "")

dic = {i: 0 for i in text}
for i in dic:
    dic[i] = text.count(i)

for i in dic:
    print(f"{i}: {dic[i]}")
