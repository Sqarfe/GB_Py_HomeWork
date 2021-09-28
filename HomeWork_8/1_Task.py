# 1.Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

import datetime

class Data:
    def __init__(self, data):
        raw = self.to_number(data)
        if self.is_valid(raw):
            self.__Day = raw[0]
            self.__Month = raw[1]
            self.__Year = raw[2]
        else:
            raise ValueError

    @property
    def get_day(self):
        return self.__Day

    @property
    def get_month(self):
        return self.__Month

    @property
    def get_year(self):
        return self.__Year


    @classmethod
    def to_number(cls, data):
        result = [int(i) for i in data.split('-')]
        return result

    @staticmethod
    def is_valid(data):
        try:
            datetime.date(data[2], data[1], data[0])
            return True
        except:
            return False


someDay = Data("28-2-1995")

print(someDay.get_day, someDay.get_month, someDay.get_year)

print(Data.is_valid(Data.to_number("28-2-1995")))
print(Data.is_valid(Data.to_number("29-2-1995")))
