immutable_var = (1, 'two', [3, 4], True)

print(immutable_var)
print(type(immutable_var)) #сам кортеж изменить нельзя, но вложенный список изменить можно
# immutable_var[0] = 2    данный код выдаст ошибку
immutable_var[2][0] = 5 # данный код изменил первый элемент вложенного списка
print(immutable_var)

mutable_list = [1, 2, 3, 4, 5]
mutable_list.append(6)
print(mutable_list)