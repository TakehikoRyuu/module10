# Блокировки и обработка ошибок
import threading
from random import randint
from time import sleep

class Bank():
    def __init__(self, balance=0):
        self.balance = int(balance)
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            dep = randint(50, 500)
            self.balance = self.balance + dep
            if self.balance >= 500 and self.lock.locked() == True:
                self.lock.release()
            print(f'Пополнение: {dep}. Баланс: {self.balance}')
            sleep(0.001)

    def take(self):
        for i in range(100):
            tak = randint(50, 500)
            print(f'Запрос на {tak}')
            if tak <= self.balance:
                self.balance = self.balance - tak
                print(f'Снятие: {tak}. Баланс: {self.balance}')
            if tak > self.balance:
                print(f'Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            sleep(0.001)


bk = Bank()
# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')