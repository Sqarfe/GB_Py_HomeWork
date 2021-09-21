# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

with open('3_Task_File.txt') as file:
    general_salary = 0
    employ_count = 0
    try:
        for line in file:
            if int(line.split()[1]) < 20000:
                print(line.split()[0])
            general_salary += int(line.split()[1])
            employ_count += 1
        print(f'Средний оклан составляет: {round(general_salary / employ_count)}')
    except:
        pass
