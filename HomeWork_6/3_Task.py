# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
#    income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
#    оклад и премия, например, {"wage": wage, "bonus": bonus}.
#
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии
#    (get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position,
#    передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    name = 'default'
    surname = 'default'
    position = 'default'
    __income = {"wage": 0, "bonus": 0}

    def set_income(self, wage, bonus):
        self.__income["wage"] = wage
        self.__income["bonus"] = bonus

    def get_wage(self):
        return self.__income["wage"]

    def get_bonus(self):
        return self.__income["bonus"]


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.set_income(wage, bonus)

    def get_full_name(self):
        return self.surname + ' ' + self.name

    def get_total_income(self):
        return self.get_bonus() + self.get_wage()


worker = Position('Sergey', 'Miroshnechenko', 'Programmer', 40000, 100000)
print(worker.name)
print(worker.surname)
print(worker.position)
print(worker.get_full_name())
print(worker.get_total_income())