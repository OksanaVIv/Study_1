# TODO Напишите функцию find_common_participants
def find_common_participants(group_1, group_2, sep_=','):
    group_1 = set(group_1.split(sep_))
    group_2 = set(group_2.split(sep_))
    list_common = list(group_1.intersection(group_2))
    list_common.sort()
    return list_common

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group,"|"))

# # TODO Провеьте работу функции с разделителем отличным от запятой
