distance_begin = int(input('Введите начальную дистанцию: '))
distance_end = int(input('Введите требуемую дистанцию: '))

i = 0
distance_current = distance_begin

while distance_current < distance_end:
    distance_current = distance_current * 1.1
    # print(f'{distance_current:.2f}')
    i += 1

print(f'Спортсмену необходимо {i} дней тренировок')


