def my_func(a, b, c):
    arr = [a, b, c]
    arr.sort(reverse=True)
    return arr[0]+arr[1]


try:
    print(f'Сумма дву больших = '
          f'{my_func(float(input("Введите a: ")), float(input("Введите b: ")), float(input("Введите c: ")))}')
except ValueError:
    print('Вы ввели некорректные данные')
