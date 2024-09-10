my_list = [42, 69, 322, 13, 0, 99]

index = 0
while index < len(my_list):
    if my_list[index] > 0:
        print(my_list[index])
        index += 1
    elif my_list[index] == 0:
        index += 1
        continue
    else:
        break

print('Перебор закончился')