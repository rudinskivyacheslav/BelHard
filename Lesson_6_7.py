# Дан список чисел, необходимо его развернуть без использования метода revese и функции reversed,
# а так же дополнительного списка и среза


def reverce_list(lst: list) -> list:
    for i in range(round(len(lst)/2)):
        lst[i], lst[~i] = lst[~i], lst[i]

    return lst


print(reverce_list([1, 2, 3, 4, 5, 6, 7, 8]))
print(reverce_list([1, 2, 3, 4, 5, 6, 7]))
