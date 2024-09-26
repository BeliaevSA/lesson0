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


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))