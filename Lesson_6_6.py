# Дан список содержащий в себе различные типы данных, отфильтровать таким образом,
# чтобы остались только строки, использование дополнительного списка незаконно
lst = [1, None, "True", {4, "Big"}, False, "Hello", (4, "Python"), [True, "Java"], 43, "Data", {1: "one", 2: "two"}]

lst = list(filter(lambda x: isinstance(x, str), lst))
print(lst)
