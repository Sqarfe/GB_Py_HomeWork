# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
#
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
#       для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
#
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта,
# проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod
import itertools


class Clothes(ABC):
    @property
    @abstractmethod
    def my_method(self):
        pass


class Coat(Clothes):
    def __init__(self, V):
        self.V = V

    @property
    def my_method(self):
        return self.V/6.5 + 0.5


class Suit(Clothes):
    def __init__(self, H):
        self.H = H

    @property
    def my_method(self):
        return 2 * self.H + 0.3


clothes = [Coat(32), Suit(1.7), Coat(33), Suit(1.8)]
total_Sum = 0
for item in clothes:
    total_Sum += item.my_method
    print(type(item).__name__ + " %.2f" % item.my_method)

print(f'total_Sum: {total_Sum:.2f}')
