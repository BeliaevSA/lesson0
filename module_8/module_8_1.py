def add_everything_up(value_one, value_two):
  try:
    return value_one + value_two
  except:
   return str(value_one) + str(value_two)

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
