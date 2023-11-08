#Пользователь вводит предложение, заменить все пробелы на "-" 2-мя способами

text1 = input("Enter text1: ")
text1 = text1.replace(" ", "-")
print(text1)

text2 = input("Enter text2: ")
list_text2 = text2.split()
text2 = "-".join(list_text2)
print(text2)
