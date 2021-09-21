# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open('5_Task_File.txt', 'w+') as file:
    while True:
        inp = input('Введите число, или пустую строку для выхода: ')
        if inp == '':
            break
        try:
            inpInt = int(inp)
            file.write(inp + ' ')
            file.seek(0)
            line = file.readline()
            lineNumbs = [int(numb) for numb in line.split()]
            print(f'Текущая сумма чисел в файле: {sum(lineNumbs)}')
        except:
            print('Argument exception')
