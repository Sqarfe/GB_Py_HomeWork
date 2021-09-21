# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет
#   и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.
#
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
import re


def find_item(text, item):
    if text.find(item) > -1:
        return int(re.split(';|,|:| ', line.split(item)[0])[-1])
    else:
        return 0


subjects = {}
with open('6_Task_File.txt') as file:
    for line in file:
        subject = line.split(':')[0]
        lectures = find_item(line, '(л)')
        practicalLessons = find_item(line, '(пр)')
        labWorks = find_item(line, '(лаб)')
        subjects[subject] = lectures+practicalLessons+labWorks
print(subjects)

