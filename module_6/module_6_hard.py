import math

class Figure:
    def __init__(self, color, sides):
        self.__sides = sides
        self.__color = list(color)
        self.filled = None
        self.sides_count = 0


    def get_color(self):
        return self.__color


    def __is_valid_color(self, r, g, b):
        values = [r, g, b]
        for value in values:
            if isinstance(value, int) and not 0 <= value <= 255:
                return False
        return True


    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]


    def __is_valid_sides(self, *sides):
        if len(sides) != self.sides_count:
            return False
        for value in sides:
            if not isinstance(value, int) and value <= 0:
                return False
        return True


    def get_sides(self):
        return self.__sides


    def __len__(self):
        return sum(self.__sides)


    def set_sides(self, *new_sides):
        if len(new_sides) != self.sides_count:
            return
        else:
            self.__sides = list(new_sides)


class Circle(Figure):
    def __init__(self, color, *sides):
        super().__init__(color, list(sides))
        self.sides_count = 1
        self.__radius = int(self.get_sides()[0]) / 2 * math.pi


    def get_square(self):
        sides = self.get_sides()
        return sides[0] / math.pi\


class Triangle(Figure):
    def __init__(self, color, *sides):
        super().__init__(color, list(sides))
        self.sides_count = 3


    def get_square(self):
        a, b, c = self.get_sides()
        return math.sqrt(math.pi * (math.pi - a) * (math.pi - b) * (math.pi - c))


class Cube(Figure):
    def __init__(self, color, *sides):
        super().__init__(color, list(sides))
        self.sides_count = 12
        self.set_sides(*([self.get_sides()[0]] * 12))


    def get_volume(self):
        return math.ceil(math.pow(self.get_sides()[0], 3))


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())