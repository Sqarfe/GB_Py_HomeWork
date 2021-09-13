month = 0
strWinter = 'Зима'
strSpring = 'Весна'
strSummer = 'Лето'
strAutumn = 'Осень'

dc = {1 : strWinter, 2 : strWinter, 12 : strWinter,
      3 : strSpring, 4 : strSpring, 5 : strSpring,
      6 : strSummer, 7 : strSummer, 8 : strSummer,
      9 : strAutumn, 10 : strAutumn, 11 : strAutumn}

while True:
    str = input('Введите месяц в виде целого числа, для завершения - введите пустую строку: ')
    if str == '':
        break
    if str.isdigit():
        month = int(str)
        if month >= 1 and month <= 12 :
            print(f'месяц {month} : {dc[month]}')
            continue
    print('Некоректный ввод!')