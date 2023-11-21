# TODO написать функцию remove
from typing import Any


def remove(start_list: list[Any], value: Any) -> list[Any]:
    index_list = []
    for i, j in enumerate(start_list):
        if j == value:
            index_list.append(i)
    if not index_list:
        raise ValueError("Значение в списке не найдено")
    index = index_list[-1]
    return start_list[:index] + start_list[index+1:]


print(remove([0, 1, 2, 0, 1, 2], 0))  # [0, 1, 2, 1, 2]
print(remove([0, 1, 2], 0))  # [1, 2]
print(remove([0, 1, 2, 3, 4], 4))  # [0, 1, 2, 3]
