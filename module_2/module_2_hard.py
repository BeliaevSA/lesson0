import random

list_numbers = list(range(3, 21))

def password_selection(n):
    # узнаем на какие числа делится данное число
    numbers = []
    for num in range(3, n + 1):
        if n % num == 0:
            numbers.append(num)

    # проходим по каждому числу деления и делаем все возможные варианты
    password = []
    for num in numbers:
        list_number = list(range(1, num))
        # print(list_number)

        for item in list_number:
            difference = num - item
            if difference > item:
                password.append(str(item) + str(difference))
            else:
                continue

    sorted_password = []
    for i in range(len(password) // 2 + 1):
        for j in range(len(password)):
            if password[j][0] == str(i + 1):
                sorted_password.append(password[j])

    result = "".join(sorted_password)

    print(f'Случайное число: {n}')
    print(f'Пароль: {result}')
    print('---------------------')
    return result

password_selection(random.choice(list_numbers))
password_selection(random.choice(list_numbers))
password_selection(random.choice(list_numbers))
password_selection(random.choice(list_numbers))