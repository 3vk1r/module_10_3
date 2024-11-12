from random import randint as rd
from time import sleep as sp
import threading as thr

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = thr.Lock()

    def deposit(self):
        for i in range(100):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            deposit = rd(50,500)
            self.balance += deposit
            print(f'Пополнение: {deposit}. Баланс: {self.balance}".')
        sp(0.001)

    def take(self):
        for i in range(100):
            take = rd(50,500)
            print(f'Запрос на {take}')
            if self.balance >= take:
                self.balance -= take
                print(f'Снятие: {take}. Баланс: {self.balance}')
            else:
                print('Запрос отклонен, недостаточно средств')
                self.lock.acquire()
        sp(0.001)


bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = thr.Thread(target=Bank.deposit, args=(bk,))
th2 = thr.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')