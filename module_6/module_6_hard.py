class Figure:

    def __init__(self):
        self.__sides = []
        self.__color = [255, 255, 255]
        self.filled = None
        sides_count = 0


    def get_color(self):
        return self.__color


    def __is_valid_color(self, r, g, b):
        values = [r, g, b]
        for value in values:
            if isinstance(value, int) and value < 0 and value > 255:
                return False
        return True


    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]


    def __is_valid_sides(self, *sides):
        if len(sides) != self.sides_count:
            return False
        # for value in sides:



class Circle(Figure):
    pass


class Triangle(Figure):
    pass


class Cube(Figure):
    pass

figure1 = Figure()
print(dir(figure1))
print(figure1.filled)
print(figure1._Figure__is_valid_sides(1, 2, 3))