my_list = [7, 5, 3, 3, 2]

while True:
    inp = input('Введите значение рэйтинга, для завершения - введите пустую строку: ')
    if inp == '':
        break
    if inp.isdigit():
        numb = int(inp)
        my_list.append(numb)
        my_list.sort(reverse = True)

        output = 'Результат: '
        for i in my_list :
            output += (f'{i}, ')
        output = output[:-2] + '.'

        print(output)
        continue
    print('Некоректный ввод!')