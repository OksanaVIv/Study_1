# # TODO написать функцию, которая выдает трехзначное число
from random import randint


def casino() -> int:
    number_list = [str(randint(0, 9)) for _ in range(3)]
    return int(''.join(number_list))


print(casino())
