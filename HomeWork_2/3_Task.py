month = 0
strWinter = 'Зима'
strSpring = 'Весна'
strSummer = 'Лето'
strAutumn = 'Осень'

list = [strWinter, strWinter, strSpring, strSpring, strSpring, strSummer, strSummer, strSummer, strAutumn, strAutumn, strAutumn, strWinter]


while True:
    str = input('Введите месяц в виде целого числа, для завершения - введите пустую строку: ')
    if str == '':
        break
    if str.isdigit():
        month = int(str)
        if month >= 1 and month <= 12 :
            print(f'месяц {month} : {list[month-1]}')
            continue
    print('Некоректный ввод!')