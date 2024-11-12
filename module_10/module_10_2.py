from threading import Thread
import time

class Knight(Thread):
  def __init__(self, name: str, power: int):
    Thread.__init__(self)
    self.name = name
    self.power = power
    self.health = 100

  def battle(self):
    count = self.health
    day = 0
    while count > 0:
      count -= self.power
      day += 1
      print(f'{self.name}, сражается {day} день(дня)..., осталось {count} воинов.')
      time.sleep(1)
    print(f'{self.name} одержал победу спустя {day} дней(дня)!')

  def run(self):
    print(f"{self.name}, на нас напали!")
    self.battle()
    

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
print('Все битвы закончились!')
