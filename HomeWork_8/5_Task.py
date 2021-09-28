# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и
# передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.
from abc import ABC, abstractmethod
import itertools


class Department:               # отделение
    department_list = {}

    captivity = 0
    storage = None
    worker = None

    def __init__(self, captivity, worker):
        self.department_list[type(self).__name__] = self
        self.captivity = captivity
        self.storage = []
        self.worker = worker

    def is_full(self):
        return len(self.storage) < self.captivity

    def is_empty(self):
        return len(self.storage) == 0

    def get_item(self, item):
        self.storage.remove(item)
        return item

    def put_item(self, item):
        self.storage.append(item)
        print(f"Товар {item} поступил в {type(self).__name__}!")


class DispatchDepartment(Department):               # отделение отправки
    def send_item(self, item):
        self.storage.remove(item)
        print(f"Товар {item} был отправлен!")


class ReceptionDepartment(Department):               # отделение приёма
    ...


class ShopHall(Department):                         # зал магазина
    def sell_item(self, item):
        self.storage.remove(item)
        print(f"Товар {item} был продан! ")


class WareHouse(Department):                       # склад
    ...


class OfficeEquipment:
    def __init__(self, title, price, weight):
        self.id = OfficeEquipment.generate_id()
        self.title = title
        self.price = price
        self.weight = weight

    @staticmethod
    def generate_id():
        last_id = 0
        while True:
            yield last_id
            last_id += 1


class Printer(OfficeEquipment):
    def __init__(self, title, price, weight, color, print_type):
        self.color = color
        self.print_type = print_type
        super().__init__(title, price, weight)


class Scanner(OfficeEquipment):
    def __init__(self, title, price, weight, speed, resolution):
        self.speed = speed
        self.resolution = resolution
        super().__init__(title, price, weight)


class Xerox(OfficeEquipment):
    def __init__(self, title, price, weight, xerox_format, is_colored):
        self.xerox_format = xerox_format
        self.is_colored = is_colored
        super().__init__(title, price, weight)


class Lamp(OfficeEquipment):
    def __init__(self, title, price, weight, brightness, lamp_type):
        self.brightness = brightness
        self.lamp_type = lamp_type
        super().__init__(title, price, weight)


class Worker:
    name = None
    tasks = []

    def __init__(self, name):
        self.name = name

    def add_task(self, item, get_place, put_place):
        self.tasks.append([item, get_place, put_place])

    def do_work(self):
        work = self.tasks.pop(0)
        item = work[1].get_item(work[0])
        print(f'Рабочий {self.name} забрал предмет {item} из {type(work[1]).__name__}')
        work[2].put_item(item)

    def has_work(self):
        return True if len(self.tasks) > 0 else False


Steve = Worker("Стив")

printer = Printer("Принтер Canon", 8000, 5, "Green", "Порошковая печать")
scanner = Scanner("Сканер dexp", 2200, 1, 2, "1920х1080")
xerox = Xerox("Ксерокс Epson", 19000, 120, "А4", "Цветной")
lamp = Lamp("Лампа Xiaomi", 1500, 120, "80w", "Светодиодная")

ware_house = WareHouse(100, Steve)
shop_hall = ShopHall(30, Steve)
dispatch_department = DispatchDepartment(3, Steve)
reception_department = ReceptionDepartment(5, Steve)

reception_department.put_item(printer)
reception_department.put_item(scanner)
reception_department.put_item(xerox)
reception_department.put_item(lamp)

for item in reception_department.storage:
    Steve.add_task(item, reception_department, ware_house)

while Steve.has_work():
    Steve.do_work()


Steve.add_task(ware_house.storage[0], ware_house, shop_hall)
Steve.add_task(ware_house.storage[1], ware_house, shop_hall)
Steve.add_task(ware_house.storage[2], ware_house, dispatch_department)
Steve.add_task(ware_house.storage[3], ware_house, dispatch_department)

while Steve.has_work():
    Steve.do_work()