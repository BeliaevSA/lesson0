# Словарь
my_dist = {'Sergey': 1994, 'Dmitriy': 1996, 'Nikolay': 1993}

print(my_dist)
print(my_dist['Sergey'])
print(my_dist.get('Nikita', 'Данного имени нет в словаре'))

my_dist.update({'Nikita': 1997, 'Evgeniy': 1990})
print(my_dist)
item = my_dist.pop('Dmitriy')
print(item)
print(my_dist)

# Множества
my_set = {10, 2.0, 3, True, 'Пять', 5, 2, 'Пять',(0, 1)}
print(my_set)
my_set.update({11, 12})
print(my_set)
print(my_set.discard(15))
print(my_set)
