class House:
    def __init__(self, name: str, numbers_of_floors: int):
        self.name = name
        self.numbers_of_floors = numbers_of_floors


    def go_to(self, new_floor: int):
        if new_floor > self.numbers_of_floors or new_floor < 1:
            print('Такого этажа не существует')
            return
        for i in range(1, new_floor + 1):
            print(i)


    def __len__(self):
        return self.numbers_of_floors


    def __str__(self):
        return f'Название: {self.name}, количество этажей: {self.numbers_of_floors}'


    def __eq__(self, other):
        if isinstance(other, House):
            return self.numbers_of_floors == other.numbers_of_floors
        elif isinstance(other, int):
            return self.numbers_of_floors == other
        else:
            return False


    def __lt__(self, other):
        if isinstance(other, House):
            return self.numbers_of_floors < other.numbers_of_floors
        elif isinstance(other, int):
            return self.numbers_of_floors < other
        else:
            return False


    def __le__(self, other):
        if isinstance(other, House):
            return self.numbers_of_floors <= other.numbers_of_floors
        elif isinstance(other, int):
            return self.numbers_of_floors <= other
        else:
            return False


    def __gt__(self, other):
        if isinstance(other, House):
            return self.numbers_of_floors > other.numbers_of_floors
        elif isinstance(other, int):
            return self.numbers_of_floors > other
        else:
            return False


    def __ge__(self, other):
        if isinstance(other, House):
            return self.numbers_of_floors >= other.numbers_of_floors
        elif isinstance(other, int):
            return self.numbers_of_floors >= other
        else:
            return False


    def __ne__(self, other):
        if isinstance(other, House):
            return self.numbers_of_floors != other.numbers_of_floors
        elif isinstance(other, int):
            return self.numbers_of_floors != other
        else:
            return False


    def __add__(self, value):
        if isinstance(value, int):
            self.numbers_of_floors += value
        if isinstance(value, House):
            self.numbers_of_floors += value.numbers_of_floors
        return self


    def __radd__(self, value):
        return self.__add__(value)


    def __iadd__(self, value):
        return self.__add__(value)


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2)  # __eq__

h1 = h1 + 10  # __add__
print(h1)
print(h1 == h2)

h1 += 10  # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__