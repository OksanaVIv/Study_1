numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

lost_index = 4

part_1 = numbers[:lost_index]
part_2 = numbers[(lost_index+1):]
average = (sum(part_1) + sum(part_2))/(len(numbers))
numbers[4] = average

print("Измененный список:", numbers)
