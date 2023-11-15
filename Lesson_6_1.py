#Написать функцию перевода десятичного числа в двоичное и обратно, без использования функции int
from math import floor


def binary_representation(value: int):
    result = ""
    while value > 0:
        result = f"{int(value % 2)}{result}"
        value = floor(value / 2)

    return int(result)


print(binary_representation(111))
print(binary_representation(1731))
print(binary_representation(255))
