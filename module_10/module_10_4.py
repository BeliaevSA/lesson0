rom threading import Thread
from queue import Queue
import time
from random import randint

class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None

class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        # Имитация времени, которое гость тратит на еду
        eating_time = randint(3, 10)
        print(f"{self.name} кушает ({eating_time} секунд)...")
        time.sleep(eating_time)
        print(f"{self.name} покушал(-а)")

class Cafe:
    def __init__(self, *tables):
        self.queue = Queue()  # Очередь гостей
        self.tables = list(tables)  # Список столов

    def guest_arrival(self, *guests):
        for guest in guests:
            table_found = False
            for table in self.tables:
                if table.guest is None:  # Если стол свободен
                    table.guest = guest
                    print(f"{guest.name} сел(-а) за стол номер {table.number}")
                    guest.start()  # Запуск потока гостя
                    table_found = True
                    break
            if not table_found:
                self.queue.put(guest)  # Если все столы заняты
                print(f"{guest.name} в очереди")

    def discuss_guests(self):
        while not self.queue.empty() or any(table.guest is not None for table in self.tables):
            for table in self.tables:
                if table.guest is not None:  # Если за столом есть гость
                    guest = table.guest
                    if not guest.is_alive():  # Проверка завершения потока
                        print(f"{guest.name} покушал(-а) и ушёл(ушла)")
                        print(f"Стол номер {table.number} свободен")
                        table.guest = None  # Освобождение стола
                        if not self.queue.empty():  # Если в очереди есть гости
                            next_guest = self.queue.get()
                            table.guest = next_guest
                            print(f"{next_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")
                            next_guest.start()  # Запуск потока нового гостя
            time.sleep(1)  # Небольшая пауза для проверки состояния потоков
        print("Все гости обслужены и кафе пустое")


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
