# Очереди для обмена данными между потоками.
from queue import Queue
from threading import Thread
from time import sleep
from random import randint


class Table():
    def __init__(self, number, guest=None):
        self.number = number
        self.guest = guest


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        sleep(randint(3, 10))


class Cafe(Table):
    def __init__(self, *tables):
        self.tables = tables
        self.queue = Queue()

    def guest_arrival(self, *guests):
        for guest in guests:
            open_table = None
            for table in self.tables:
                if table.guest is None:
                    open_table = table
                    break
                else:
                    open_table = None
            if open_table != None:
                open_table.guest = guest
                print(f'{guest.name} сел(-а) за стол номер {open_table.number}')
            if open_table == None:
                self.queue.put(guest)
                print(f'{guest.name} в очереди')

    def discuss_guests(self):
        while any(table.guest is not None for table in self.tables) or not self.queue.empty():
            for table in self.tables:

                if table.guest is None: # пустые столы
                    if not self.queue.empty():
                        que = self.queue.get()
                        table.guest = que
                        print(f'{que.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                        que.start()

                if table.guest is not None: # кто то есть за столом
                    if not table.guest.is_alive():
                        print(f'{table.guest.name} за {table.number} покушал(-а) и ушёл(ушла)')
                        print(f'Стол номер {table.number} свободен')
                        table.guest = None



# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей(потоков)
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()