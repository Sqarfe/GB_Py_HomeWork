def myDivision (a, b):
    try:
        return float(a)/float(b)
    except ZeroDivisionError:
        return 'ZeroDivisionError'
    except ValueError:
        return 'ValueError'


a = input('Введите число a: ')
b = input('Введите число б: ')


print(f'Результат деления: {myDivision(a, b)}')
