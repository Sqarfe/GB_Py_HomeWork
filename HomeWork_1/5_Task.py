numb_plus = int(input('Введите выручку фирмы: '))
numb_minus = int(input('Введите издержки фирмы: '))
numb_result = numb_plus - numb_minus
if numb_result > 0 :
    print(f'Выручка составила болше, чем издержки.')
    print(f'Рентабельность выручки: {numb_plus/numb_minus:.2f}')
    employeeCount = int(input('Введите колличество сотрудников: '))
    print(f'Прибыль каждого сотрудника составила: {(numb_plus-numb_minus)/employeeCount:.2f}')
else:
    print(f'Выручка составила меньше, чем издержки.')
