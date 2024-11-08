first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(value) for value in first_strings if len(value) > 5]
second_result = [(first_value, second_value) for first_value in first_strings for second_value in second_strings if len(first_value) == len(second_value)]
third_result = {value: len(value) for value in first_strings + second_strings if len(value) % 2 == 0}

print(first_result)
print(second_result)
print(third_result)
