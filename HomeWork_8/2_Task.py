# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать
#   эту ситуацию и не завершиться с ошибкой.

class MyZeroDivisionError(Exception):
    def __init__(self):
        print("Делить на ноль запрещено!")


def zero_division_catcher(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ZeroDivisionError:
            raise MyZeroDivisionError
    return wrapper


@zero_division_catcher
def divide(a, b):
    return a / b


while True:
    inp = input("Введите число, на которое Вы хотите поделить 100 или 'q' для завершения: ")
    if inp == 'q':
        break
    else:
        try:
            print(f'Ответ: {divide(100, float(inp)):.2f}')
        except MyZeroDivisionError:
            pass
