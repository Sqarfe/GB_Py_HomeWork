# 4. Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы:go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    speed = 0
    color = [0, 0, 0]
    name = 'default'
    is_police = False

    def go(self):
        self.speed = 20
        print(f'Машина {self.name} начала движение.')

    def set_speed(self, speed):
        if speed < 0:
            print('speed value error')
            return
        self.speed = speed
        print(f'Машина {self.name} едет со скоростью {self.speed}.')

    def stop(self):
        self.speed = 0
        print(f'Машина {self.name} остановилась')

    def turn(self, direction):
        print(f'Машина {self.name} повернула на {direction}')

    def show_speed(self):
        print(f'Машина {self.name} едет со скоростью {self.speed}')

    def __str__(self):
        return f'Машина: {self.name}, Цвет: {self.color}, Скорость {self.speed}, Полицейчкася машина?: {self.is_police}'


class TownCar(Car):
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def set_speed(self, speed):
        Car.set_speed(self, speed)
        if self.speed > 60:
            print(f'Машина {self.name} привысила скорость, max speed = 60')

    def __str__(self):
        return f'Класс машины: Городская, ' + Car.__str__(self)


class SportCar(Car):
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self):
        return f'Класс машины: Спортивная, ' + Car.__str__(self)


class WorkCar(Car):
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def set_speed(self, speed):
        Car.set_speed(self, speed)
        if self.speed > 40:
            print(f'Машина {self.name} привысила скорость, max speed = 40')

    def __str__(self):
        return f'Класс машины: Рабочая, ' + Car.__str__(self)


class PoliceCar(Car):
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.is_police = True

    def __str__(self):
        return f'Класс машины: Полицейская, ' + Car.__str__(self)


sportCar = SportCar('Maclaren F1', [255, 0, 0])
workCar = WorkCar('Грузовик', [255, 255, 0])
policeCar = PoliceCar('Полиция, Toyota Prius', [255, 0, 255])
townCar = TownCar('Автобус', [0, 0, 255])

sportCar.go()
sportCar.set_speed(120)
sportCar.turn('Лево')
sportCar.set_speed(-30)
sportCar.show_speed()
sportCar.stop()

townCar.go()
townCar.set_speed(110)
townCar.show_speed()
townCar.set_speed(110)


print(sportCar)
print(workCar)
print(policeCar)
print(townCar)