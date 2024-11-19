from threading import Thread, Lock
from random import randint
import time

class Bank():
  def __init__(self):
    self.balance = 0
    self.lock = Lock()


  def deposit(self):
    count = 100
    while count > 0:
      value = randint(50, 500)
      self.balance += value
      count -= 1
      if self.balance >= 500 and self.lock.locked():
        self.lock.release()
      print(f"Пополнение: {value}. Баланс: {self.balance}")
      time.sleep(0.001)

  def take(self):
    count = 100
    while count > 0:
      value = randint(50, 500)
      print(f"Запрос на {value}")
      if value < self.balance:
        self.balance -= value
        count -= 1
        print(f"Снятие: {value}. Баланс: {self.balance}")
      if value > self.balance:
        self.lock.acquire()
        print("Запрос отклонён, недостаточно средств")
      time.sleep(0.001)

b1 = Bank()
thread_deposit = Thread(target=Bank.deposit, args=(b1,))
thread_take = Thread(target=Bank.take, args=(b1,))


thread_deposit.start()
thread_take.start()
thread_deposit.join()
thread_take.join()

print(f'Итоговый баланс: {b1.balance}')
