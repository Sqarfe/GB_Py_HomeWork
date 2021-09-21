# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().
from random import randrange
from functools import reduce
import math

arr = [randrange(100, 1001) for i in range(4)]

print(arr)
print(reduce(lambda a, b: a*b, arr))
