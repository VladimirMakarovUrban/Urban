import threading
import time

class Knight(threading.Thread):
    def __init__(self, name, power):
#        self.name = name
#        self.power = power
        threading.Thread.__init__(self)
        self.name = name
        self.power = power



    def run(self):
        print(self.name, 'На нас напали')
        enemies = 100
        day = 0
        while enemies != 0:
            enemies -= self.power
            time.sleep(1)
            day += 1

            print(f"{self.name} сражается {day} день, осталось {enemies}.")
        print(f'{self.name} одержал победу спустя {day} дней(дня)!')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()