from random import sample
import string


def get_random_password() -> str:
    list_passw = sample((string.ascii_letters + string.digits), k=8)
    list_str_passw = [str(i) for i in list_passw]
    return ''.join(list_str_passw)


print(get_random_password())
