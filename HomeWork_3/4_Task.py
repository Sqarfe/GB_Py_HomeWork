'''Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y.
Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.'''

# from math import pow

def my_exponentiation(a, b):
    ans = a
    for i in range(1, -b):
        ans = ans*ans
    return 1/ans



while True:
    x = input('Введите действительное положительное число x: ')
    y = input('Введите целое отрицательное число y: ')

    try:
        floatX = float(x)
        intY = int(y)
        if (floatX > 0) and (intY < 0):
            print(f'Ответ my_funct: {my_exponentiation(floatX, intY)}')
            # print(f'Ответ Math.pow: {pow(floatX,intY)}')
        else:
            print('Неправильный знак у чисел')
    except ValueError:
        print('Неправильный тип чисел')
