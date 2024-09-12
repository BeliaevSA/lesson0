
calls = 0
def count_calls():
    global calls
    calls += 1


def string_info(string):
    result = (len(string), string.upper(), string.lower())
    count_calls()
    return result


def is_contains(string: str, list_: list):
    result = False
    for item in list_:
        if type(item) == str and string.lower() == item.lower():
            result = True
            break
    count_calls()
    return result


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)