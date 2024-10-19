from idlelib.iomenu import encoding
from pprint import pprint

def custom_write(file_name: str, strings: list):
    open_file_for_read = open(file_name, 'r', encoding='utf-8')
    count_new_line = 0
    for line in open_file_for_read.read():
        if line == '\n':
            count_new_line += 1

    open_file_for_read.close()
    open_file_for_write = open(file_name, 'a', encoding='utf-8')
    strings_positions = {}
    for string in strings:
        count_new_line += 1
        tell = open_file_for_write.tell()
        open_file_for_write.write(string + '\n')
        strings_positions.update({(count_new_line,tell): string})

    open_file_for_write.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('dict_strings.txt', info)
for elem in result.items():
    print(elem)