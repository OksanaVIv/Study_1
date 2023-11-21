from random import randint


def get_unique_list_numbers() -> list[int]:
    a = set()
    while len(a) < 16:
        a.add(randint(-10, 10))
    return list(a)
    # TODO написать функцию для получения списка уникальных целых чисел


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
