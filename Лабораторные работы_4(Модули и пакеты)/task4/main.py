from random import choice


EAGLE = "Орел"
TAILS = "Решка"

coin = [EAGLE, TAILS]  # монета, для которой нужно выбрать случайную сторону
counts = [10, 100, 1000, 100000, 1000000]  # различное количество подбрасываний
list_freq = []  # список, где будем хранить отношение количества выпавших орлов к решке

for count in counts:
    eagle_count = 0
    tails_count = 0
    for _ in range(count):
        if choice(coin) == EAGLE:
            eagle_count += 1
        else:
            tails_count += 1
    if eagle_count > tails_count:
        list_freq.append(eagle_count / tails_count)
    else:
        list_freq.append(eagle_count / tails_count)
# TODO подсчитать количество выпаданий орлов и решек)

print(list_freq)
