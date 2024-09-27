# Потоки на классах
from threading import Thread
from time import sleep
class Knight():
    def __init__(self, name, power):
        self.name = str(name)
        self.power = int(power)

    def run(self):
        war = 100
        day = 0
        print(f'{self.name}, на нас напали!')
        while war > 1:
            day += 1
            war = war - self.power
            print(f'{self.name} сражается {day} день(дня), осталось {war} воинов.')
            if war <= 0:
                print(f'{self.name} одержал победу спустя {day} дней(дня)!')
            sleep(1)


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)

th1 = Thread(target=Knight.run, args=(first_knight, ))
th2 = Thread(target=Knight.run, args=(second_knight, ))

th1.start()
th2.start()

th1.join()
th2.join()
print('Все битвы закончились!')