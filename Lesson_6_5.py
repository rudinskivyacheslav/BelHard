# Дан список чисел и на вход поступает число N, необходимо сместить список на указанное число, пример:
# [1,2,3,4,5,6,7] N=3 ответ: [5,6,7,1,2,3,4]
from collections import deque


def rotate(offset: int, lst: list):
    list_deque = deque(lst)
    list_deque.rotate(offset)
    return list(list_deque)


print(rotate(3, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(rotate(-4, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
