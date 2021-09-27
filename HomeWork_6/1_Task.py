# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
#       третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.

# Задачу можно усложнить, реализовав проверку порядка режимов,
#   и при его нарушении выводить соответствующее сообщение и завершать скрипт.

import time
from threading import Thread

class TrafficLight:
    __color = "красный"

    def running(self):
        __colors = ["красный", "желтый", "зеленый"]
        self.__color = __colors[0]
        time.sleep(7)
        self.__color = __colors[1]
        time.sleep(2)
        self.__color = __colors[2]
        time.sleep(7)

    def get_color(self):
        return self.__color


stop = False


def show_current_color():
    while not stop:
        time.sleep(0.05)
        print("\r" + light.get_color(), end='')


light = TrafficLight()

thread_color_checker = Thread(target=show_current_color)
thread_traffic_light_worker = Thread(target=light.running)

thread_color_checker.start()
thread_traffic_light_worker.start()

thread_traffic_light_worker.join()

stop = True