data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def is_tuple_or_set_or_list(value):
  return isinstance(value, tuple | set | list)


def processing_the_value(value, list_):
  number = value
  if isinstance(value, str):
    number = len(value)
  return list_.append(number)


def unpacked_fn(list_, value_list):
  for item in list_:
    if is_tuple_or_set_or_list(item):
      unpacked_fn(list(item), value_list)
    elif isinstance(item, dict):
      for key, value in item.items():
        processing_the_value(key, value_list)
        if is_tuple_or_set_or_list(item):
          unpacked_fn(list(value), value_list)
        else:
          processing_the_value(value, value_list)
    else:
      processing_the_value(item, value_list)


def fn(list_):
  value_list = []
  unpacked_fn(list_, value_list)
  return sum(value_list)


print(fn(data_structure))