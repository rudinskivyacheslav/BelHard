#Заполнить список степенями числа 2 (от 2^1 до 2^n)

n = int(input("Enter n: "))
lst = [2**i for i in range(1, n+1)]

for i, v in enumerate(lst):
    print(f"2^{i+1} = {v}")
