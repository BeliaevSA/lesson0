class Eagle:
    y_distance = 0
    sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy: int):
        self.y_distance += dy
        return self.y_distance


class Horse(Eagle):
    x_distance = 0
    sound = "Frrr"

    def get_sound(self):
        if isinstance(self, Pegasus):
            return super().sound
        else:
            return self.sound


    def run(self, dx: int):
        self.x_distance += dx
        return self.x_distance


class Pegasus(Horse, Eagle):
    def __init__(self):
        super().x_distance
        super().y_distance
        super().get_sound


    def voice(self):
        print(super().get_sound())


    def move(self, dx: int, dy: int):
        (self.run(dx), self.fly(dy))


    def get_pos(self):
        return (self.x_distance, self.y_distance)


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()