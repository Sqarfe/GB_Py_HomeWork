# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
#   изученных на уроках по ООП.

import random
import time
import sys

import PyQt6.QtCore
from PyQt6 import QtCore, QtGui, QtWidgets

import design


class Department:               # отделение
    department_list = {}
    captivity = 0
    storage = None
    items_expected = 0

    def __init__(self, captivity, progress_bar_id):
        self.department_list[type(self).__name__] = self
        self.captivity = captivity
        self.progress_bar_id = progress_bar_id
        self.storage = {}

    def has_free_space(self):
        quantity = self.items_expected
        for __item in self.storage.items():
            quantity += __item[1]
        return self.captivity-quantity

    def count_items(self):
        quantity = 0
        for __item in self.storage.items():
            quantity += __item[1]
        return quantity

    def is_empty(self):
        return len(self.storage) == 0

    def get_item(self, __item):
        self.storage[__item] -= 1
        if self.storage[__item] == 0:
            del self.storage[__item]
        Manager.entity.any_signal.emit(str(self.count_items()), self.progress_bar_id)
        return __item

    def get_random_id(self):
        __id = random.choice(list(self.storage.keys()))
        if self.storage[__id] == 0:
            del self.storage[__id]
        return __id

    def put_item(self, __item, quantity):
        if not self.has_free_space() >= quantity:
            Manager.entity.any_signal.emit(f'В отделении {type(self).__name__} недостаточно места!', 0)
            return
        if self.storage.__contains__(__item):
            self.storage[__item] += quantity
        else:
            self.storage[__item] = quantity
        Manager.entity.any_signal.emit(f"Товар '{OfficeEquipment.get_name(__item)}' поступил в {type(self).__name__}!", 0)
        Manager.entity.any_signal.emit(str(self.count_items()), self.progress_bar_id)


class DispatchDepartment(Department):               # отделение отправки
    @staticmethod
    def send_item(item, quantity, address):
        dep = Department.department_list['DispatchDepartment']
        dep.storage[item] -= quantity
        if dep.storage[item] == 0:
            del dep.storage[item]
        Manager.entity.any_signal.emit(f"Товар '{OfficeEquipment.get_name(item)}' в колличестве {quantity}шт. "
                                       f"был выслан по адресу: {address}! ", 0)
        Manager.entity.any_signal.emit(str(dep.count_items()), dep.progress_bar_id)


class ReceptionDepartment(Department):               # отделение приёма
    ...


class ShopHall(Department):                         # зал магазина
    @staticmethod
    def sell_item(item, quantity):
        dep = Department.department_list['ShopHall']
        dep.storage[item] -= quantity
        if dep.storage[item] == 0:
            del dep.storage[item]
        Manager.entity.any_signal.emit(f"Товар '{OfficeEquipment.get_name(item)}' в колличестве {quantity}шт. "
                                       f"был продан! ", 0)
        Manager.entity.any_signal.emit(str(dep.count_items()), dep.progress_bar_id)


class WareHouse(Department):                       # склад
    ...


class OfficeEquipment:
    catalog = {}
    __last_id = 0

    def __init__(self, title, price, weight):
        self.id = OfficeEquipment.get_next_id()
        self.title = title
        self.price = price
        self.weight = weight

    @staticmethod
    def get_next_id():
        OfficeEquipment.__last_id += 1
        return int(OfficeEquipment.__last_id)

    @staticmethod
    def get_name(__id):
        return OfficeEquipment.catalog[__id][0]


class Printer(OfficeEquipment):
    def __init__(self, title, price, weight, color, print_type):
        self.color = color
        self.print_type = print_type
        super().__init__(title, price, weight)
        OfficeEquipment.catalog[self.id] = [title, price, weight, color, print_type]


class Scanner(OfficeEquipment):
    def __init__(self, title, price, weight, speed, resolution):
        self.speed = speed
        self.resolution = resolution
        super().__init__(title, price, weight)
        OfficeEquipment.catalog[self.id] = [title, price, weight, speed, resolution]


class Xerox(OfficeEquipment):
    def __init__(self, title, price, weight, xerox_format, is_colored):
        self.xerox_format = xerox_format
        self.is_colored = is_colored
        super().__init__(title, price, weight)
        OfficeEquipment.catalog[self.id] = [title, price, weight, xerox_format, is_colored]


class Lamp(OfficeEquipment):
    def __init__(self, title, price, weight, brightness, lamp_type1):
        self.brightness = brightness
        self.lamp_type = lamp_type1
        super().__init__(title, price, weight)
        OfficeEquipment.catalog[self.id] = [title, price, weight, brightness, lamp_type1]


class Custom(OfficeEquipment):
    def __init__(self, title, price, weight, description):
        self.description = description
        super().__init__(title, price, weight)
        OfficeEquipment.catalog[self.id] = [title, price, weight, description]


class Worker(PyQt6.QtCore.QThread):
    any_signal = QtCore.pyqtSignal(str)
    fired = False
    do_job = False
    name = None
    speed = None
    is_free = True
    __job_default_time = 5
    __item = None
    __target = None
    __source = None
    __time_start = None

    def __init__(self, name, speed, signal):
        if len(Manager.workers) == 8:
            Manager.entity.any_signal.emit('Слишком много рабочих', 0)
            return
        super(Worker, self).__init__()
        self.any_signal.connect(signal)
        self.speed = speed
        self.name = name
        self.start()
        Manager.add_worker(self)
        self.any_signal.emit(f'Рабочй {name} прибыл на работу!')

    def set(self, item: int, target: Department, source: Department):
        self.__item = item
        self.__target = target
        self.__source = source

    def run(self):
        while not self.fired:
            if self.do_job: #and self.is_free:
                self.is_free = False
                self.__do_work()
                self.is_free = True
                self.do_job = False
            time.sleep(0.1)

    def do_work(self):
        self.do_job = True

    def __do_work(self):
        self.__source.get_item(self.__item)
        self.__target.items_expected += 1
        self.any_signal.emit(f"Рабочий {self.name} забрал предмет '{OfficeEquipment.get_name(self.__item)}' "
              f"из {type(self.__target).__name__}")
        self.__time_start = time.perf_counter()
        time.sleep(Worker.__job_default_time/self.speed)
        self.__target.items_expected -= 1
        self.__target.put_item(self.__item, 1)

    def get_progress(self):
        if not self.is_free:
            __progress = int((time.perf_counter() - self.__time_start)/(Worker.__job_default_time/self.speed)*10+0.5)
            return '#'*__progress + '_'*(10-__progress)
        else:
            return 'CoffeeTime'


class Manager(PyQt6.QtCore.QThread):
    entity = None
    any_signal = QtCore.pyqtSignal(str, int)
    need_do_primary_work = True
    workers = []
    __custom_work = []

    def __init__(self, signal):
        super(Manager, self).__init__()
        self.any_signal.connect(signal)
        Manager.entity = self
        self.start()

    def run(self):
        while True:
            if self.need_do_primary_work:
                self.do_work_primary_work()
            self.do_work_custom_work()
            self.print_job_status()
            time.sleep(0.5)

    @staticmethod
    def add_worker(worker: Worker):
        Manager.workers.append(worker)

    def do_work_primary_work(self):
        while not self.__do_primary_work():
            time.sleep(0.1)
        time.sleep(0.1)

    def do_work_custom_work(self):
        while not self.__do_custom_work():
            time.sleep(0.1)
        time.sleep(0.1)

    def __do_primary_work(self):
        while True:
            self.print_job_status()
            job = Manager.get_primary_work()
            if not job:
                if not Manager.is_job_done():
                    time.sleep(0.1)
                    continue
                else:
                    return True
            worker: Worker = Manager.get_free_worker()
            if worker:
                worker.is_free=False
                worker.set(*job)
                worker.do_work()
            time.sleep(0.2)

    def __do_custom_work(self):
        while len(Manager.__custom_work) != 0:
            self.print_job_status()
            job = Manager.__custom_work[0]
            if not job[3].has_free_space():
                del Manager.__custom_work[0]
                continue
            worker: Worker = Manager.get_free_worker()
            if worker:
                job[1] -= 1
                if job[1] == 0:
                    del Manager.__custom_work[0]
                worker.set(job[0], job[3], job[2])
                worker.do_work()
            time.sleep(0.1)
        return True

    def print_job_status(self):
        status = ''
        for worker in Manager.workers:
            status += '['+worker.get_progress()+'] '
        self.any_signal.emit(status, 1)

    @staticmethod
    def get_free_worker():
        for worker in Manager.workers:
            if worker.is_free:
                return worker
        return False

    @staticmethod
    def check_work(depart_target: Department, depart_source: Department):
        if depart_target.has_free_space() and not depart_source.is_empty():
            return depart_source.get_random_id(), depart_target, depart_source
        else:
            return False

    @staticmethod          # WareHouse ShopHall DispatchDepartment ReceptionDepartment
    def get_primary_work():
        __work = Manager.check_work(Department.department_list['ShopHall'],
                                    Department.department_list['ReceptionDepartment'])
        if __work:
            return __work
        __work = Manager.check_work(Department.department_list['WareHouse'],
                                    Department.department_list['ReceptionDepartment'])
        if __work:
            return __work
        __work = Manager.check_work(Department.department_list['ShopHall'],
                                    Department.department_list['WareHouse'])
        if __work:
            return __work
        return False

    @staticmethod
    def add_custom_work(item: int, quantity: int, depart_source: Department, depart_target: Department):
        Manager.__custom_work.append([item, quantity, depart_source, depart_target])

    @staticmethod
    def is_job_done():
        flag = True
        for worker in Manager.workers:
            flag = flag and worker.is_free
        return flag


class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    __entity = None

    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        ExampleApp.__entity = self

        # Events:
        self.pushButton_16.clicked.connect(self.add_item)
        self.pushButton_3.clicked.connect(self.add_worker)
        self.pushButton_2.clicked.connect(self.set_speed_worker)
        self.pushButton_4.clicked.connect(self.remove_worker)
        self.pushButton_5.clicked.connect(self.add_custom)
        self.pushButton.clicked.connect(self.refresh_add_work_source)
        self.comboBox_4.currentIndexChanged.connect(self.refresh_add_work_items)
        self.tabWidget.currentChanged.connect(self.refresh_workers)
        self.checkBox.stateChanged.connect(self.set_primary_work_light)
        self.comboBox_2.currentIndexChanged.connect(self.refresh_add_work_source_spin)

        self.tabWidget_2.currentChanged.connect(self.sell_send_form_local_update_items)

        self.pushButton_9.clicked.connect(self.sell_send_form_local_update_items)
        self.comboBox_5.currentTextChanged.connect(self.sell_form_local_update_spin)
        self.pushButton_6.clicked.connect(self.sell_item)

        self.pushButton_11.clicked.connect(self.sell_send_form_local_update_items)
        self.comboBox_6.currentTextChanged.connect(self.send_form_local_update_spin)
        self.pushButton_7.clicked.connect(self.send_item)

        # btm init end=
        # comboBox_init
        self.comboBox_8.addItems(['Добавить принтер',
                                  'Добавить сканер',
                                  'Добавить ксерокс',
                                  'Добавить лампу',
                                  'Добавить другой товар',
                                  'Добавить существующий'])
        self.comboBox_8.currentTextChanged.connect(self.on_select_new_item)
        self.comboBox_7.setDisabled(True)
        # comboBox_init end

        # validators
        int_validator = QtGui.QIntValidator(self)
        self.lineEdit_38.setValidator(int_validator)
        self.lineEdit_32.setValidator(int_validator)
        self.spinBox_3.setRange(1, 5)
        # end valid

        # init
        ware_house = WareHouse(60, 2)
        shop_hall = ShopHall(20, 3)
        reception_department = ReceptionDepartment(15, 4)
        dispatch_department = DispatchDepartment(5, 5)

        self.progressBar.setRange(0, ware_house.captivity)
        self.progressBar_2.setRange(0, shop_hall.captivity)
        self.progressBar_3.setRange(0, reception_department.captivity)
        self.progressBar_4.setRange(0, dispatch_department.captivity)

        self.threads = {}

        Worker("Стивен", 3, self.my_function)
        self.threads[1] = Manager(self.my_function)

        printer_id = Printer("Принтер Canon", 8000, 5, "Green", "Порошковая печать").id
        scanner_id = Scanner("Сканер dexp", 2200, 1, 2, "1920х1080").id
        xerox_id = Xerox("Ксерокс Epson", 19000, 120, "А4", "Цветной").id
        lamp_id = Lamp("Лампа Xiaomi", 1500, 120, "80w", "Светодиодная").id

        reception_department.put_item(printer_id, 1)
        reception_department.put_item(scanner_id, 2)
        reception_department.put_item(xerox_id, 1)
        reception_department.put_item(lamp_id, 1)

    def sell_send_form_local_update_items(self):
        self.comboBox_5.clear()
        self.comboBox_6.clear()
        dep: Department = Department.department_list['ShopHall']
        dep2: Department = Department.department_list['DispatchDepartment']
        items = [f'{key}: {OfficeEquipment.catalog[key][0]}' for key in dep.storage.keys()]
        items2 = [f'{key}: {OfficeEquipment.catalog[key][0]}' for key in dep2.storage.keys()]
        if len(items) != 0:
            self.comboBox_5.addItems(items)
        if len(items2) != 0:
            self.comboBox_6.addItems(items2)

    def sell_form_local_update_spin(self):
        if self.comboBox_5.currentText() == '':
            return
        dep: Department = Department.department_list["ShopHall"]
        quantity = dep.storage[int(self.comboBox_5.currentText().split(':')[0])]
        self.spinBox_2.setValue(quantity)
        self.spinBox_2.setRange(1, quantity)
        self.spinBox_2.setDisabled(False)
        self.pushButton_6.setDisabled(False)

    def send_form_local_update_spin(self):
        if self.comboBox_6.currentText() == '':
            return
        dep: Department = Department.department_list["DispatchDepartment"]
        quantity = dep.storage[int(self.comboBox_6.currentText().split(':')[0])]
        self.spinBox_4.setValue(quantity)
        self.spinBox_4.setRange(1, quantity)
        self.spinBox_4.setDisabled(False)
        self.pushButton_7.setDisabled(False)

    def send_item(self):
        DispatchDepartment.send_item(int(self.comboBox_6.currentText().split(':')[0]), self.spinBox_4.value(),
                                     self.lineEdit_3.text())
        self.sell_send_form_local_update_items()
        self.pushButton_7.setDisabled(True)

    def sell_item(self):
        ShopHall.sell_item(int(self.comboBox_5.currentText().split(':')[0]), self.spinBox_2.value())
        self.sell_send_form_local_update_items()
        self.pushButton_6.setDisabled(True)

    def sell_form_local_update_items(self):
        self.comboBox_5.clear()
        dep: Department = Department.department_list['ShopHall']
        items = [f'{key}: {OfficeEquipment.catalog[key][0]}' for key in dep.storage.keys()]
        if len(items) == 0:
            return
        self.comboBox_5.addItems(items)

    def set_primary_work_light(self):
        Manager.need_do_primary_work = self.checkBox.isChecked()

    def my_function(self, text, item_id=0):
        if item_id == 0:
            self.plainTextEdit.appendPlainText(text)
        if item_id == 1:
            self.lineEdit.setText(text)
        if item_id == 2:
            self.progressBar.setValue(int(text))
        if item_id == 3:
            self.progressBar_2.setValue(int(text))
        if item_id == 4:
            self.progressBar_3.setValue(int(text))
        if item_id == 5:
            self.progressBar_4.setValue(int(text))

        if not Manager.is_job_done():
            self.pushButton.setDisabled(True)
            self.comboBox_4.setDisabled(True)
            self.comboBox_2.setDisabled(True)
            self.spinBox.setDisabled(True)
            self.comboBox_3.setDisabled(True)
            self.pushButton_5.setDisabled(True)
        else:
            self.pushButton.setDisabled(False)

    def set_speed_worker(self):
        worker = Manager.workers[self.comboBox.currentIndex()]
        worker.speed = self.doubleSpinBox_2.value()
        self.plainTextEdit.appendPlainText(worker.name + 'теперь работает со скоростью ' + str(worker.speed))

    def remove_worker(self):
        if len(Manager.workers) == 0:
            return
        worker: Worker = Manager.workers.pop(self.comboBox.currentIndex())
        worker.fired = True
        self.plainTextEdit.appendPlainText(f'Рабочий {worker.name} был уволен!')
        Manager.print_job_status(self.threads[1])
        self.refresh_workers()

    def refresh_workers(self):
        self.comboBox.clear()
        items = [worker.name for worker in Manager.workers]
        self.comboBox.addItems(items)
        Manager.print_job_status(self.threads[1])

    def add_worker(self):
        name = 'NoName' if self.lineEdit_2.text() == '' else self.lineEdit_2.text()
        Worker(name, self.doubleSpinBox.value(), self.my_function)
        self.refresh_workers()

    def on_select_new_item(self, value):
        fields = [self.lineEdit_36, self.lineEdit_38, self.lineEdit_32, self.lineEdit_39, self.lineEdit_37]
        self.clear_input(fields)
        index = self.comboBox_8.currentIndex()
        if index <= 4:
            [field.setDisabled(False) for field in fields]
            self.comboBox_7.setDisabled(True)

        if index == 0:
            fields[3].setPlaceholderText('Цвет')
            fields[4].setPlaceholderText('Тип печати')
        if index == 1:
            fields[3].setPlaceholderText('Скорость сканирования')
            fields[4].setPlaceholderText('Разрешение')
        if index == 2:
            fields[3].setPlaceholderText('Формат бумаги')
            fields[4].setPlaceholderText('Цветной')
        if index == 3:
            fields[3].setPlaceholderText('Яркость')
            fields[4].setPlaceholderText('Тип лампы')
        if index == 4:
            fields[3].setPlaceholderText('Описание товара')
            fields[4].setDisabled(True)
        if index == 5:
            [field.setDisabled(True) for field in fields]
            self.comboBox_7.setDisabled(False)
            self.refresh_exist_item()

    def add_item(self):
        params = [self.lineEdit_36, self.lineEdit_38, self.lineEdit_32, self.lineEdit_39, self.lineEdit_37]
        params = [p.text() for p in params]
        index = self.comboBox_8.currentIndex()
        item_id = -1
        if not index == 5:
            if not self.is_input_valid(params):
                return
        if index == 0:
            item_id = Printer(*params).id
        if index == 1:
            item_id = Scanner(*params).id
        if index == 2:
            item_id = Xerox(*params).id
        if index == 3:
            item_id = Lamp(*params).id
        if index == 4:
            item_id = Custom(*params[:4]).id
        if index == 5:
            item_id = int(self.comboBox_7.currentText().split(':')[0])

        Department.department_list['ReceptionDepartment'].put_item(item_id, int(self.spinBox_3.text()))

    def is_input_valid(self, params):
        text_params = [params[0], params[3], params[4]]
        int_params = [params[1], params[2]]
        text_params = params[:2] if self.comboBox_8.currentIndex() == 4 else text_params
        self.lineEdit_40.setText('')
        for p in text_params:
            if len(p) < 3 or len(p) > 15:
                self.lineEdit_40.setText('Длинна текста должна составлять 3-15 символов')
                return False
        for p in int_params:
            if int(p) < 0:
                self.lineEdit_40.setText('Значения цены/веса неверны')
                return False
        return True

    def clear_input(self, fields):
        for f in fields:
            f.setText('')

    def refresh_exist_item(self):
        self.comboBox_7.clear()
        items = [f'{key}: {val[0]}' for key, val in OfficeEquipment.catalog.items()]
        self.comboBox_7.addItems(items)

    def refresh_add_work_source(self):
        self.comboBox_4.clear()
        items = [key for key, val in Department.department_list.items() if not val.is_empty()]
        self.comboBox_4.addItems(items)
        if len(items) == 0:
            self.comboBox_4.setDisabled(True)
            return
        self.comboBox_4.setDisabled(False)

    def refresh_add_work_items(self):
        if self.comboBox_4.currentText() == '':
            return
        dep: Department = Department.department_list[self.comboBox_4.currentText()]
        items = [f'{key}: {OfficeEquipment.catalog[key][0]}' for key in dep.storage.keys()]
        if len(items) == 0:
            self.comboBox_2.setDisabled(True)
            return
        self.comboBox_2.clear()
        self.comboBox_2.addItems(items)
        self.comboBox_2.setDisabled(False)

    def refresh_add_work_source_spin(self):
        if self.comboBox_2.currentText() == '':
            return
        dep: Department = Department.department_list[self.comboBox_4.currentText()]
        quantity = dep.storage[int(self.comboBox_2.currentText().split(':')[0])]
        self.spinBox.setValue(quantity)
        self.spinBox.setRange(1, quantity)
        self.spinBox.setDisabled(False)
        self.refresh_add_work_target()

    def refresh_add_work_target(self):
        self.comboBox_3.clear()
        items = [f'{key}' for key in Department.department_list.keys() if key != self.comboBox_4.currentText()]
        self.comboBox_3.addItems(items)
        self.comboBox_3.setDisabled(False)
        self.pushButton_5.setDisabled(False)

    def add_custom(self):
        item = int(self.comboBox_2.currentText().split(':')[0])
        quantity = self.spinBox.value()
        source = Department.department_list[self.comboBox_4.currentText()]
        target = Department.department_list[self.comboBox_3.currentText()]
        Manager.add_custom_work(item, quantity, source, target)
        self.comboBox_4.setDisabled(True)
        self.comboBox_2.setDisabled(True)
        self.spinBox.setDisabled(True)
        self.comboBox_3.setDisabled(True)
        self.pushButton_5.setDisabled(True)


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
