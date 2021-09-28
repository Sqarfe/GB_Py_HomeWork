# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и
# передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.

class WareHouse:
    def __init__(self, size):
        self.size = size


class OfficeEquipment:
    def __init__(self, title, price, weight):
        self.title = title
        self.price = price
        self.weight = weight


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
