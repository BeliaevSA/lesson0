first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(values[0]) - len(values[1]) if len(values[0]) > len(values[1]) else len(values[1]) - len(values[0]) for values in zip(first, second) if len(values[0]) != len(values[1]))

second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))


print(list(first_result))
print(list(second_result))
