# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

arr = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре', 'Five': 'Пять',
       'Six': 'Шесть', 'Seven': 'Семь', 'Eight': 'Восемь', 'Nine': 'Девять', 'Ten': 'Десять'}


def str_converter(txt, mp):
    for key, val in mp.items():
        if txt.find(key) >= 0:
            txt = txt.replace(key, val)
    return txt


with open('4_Task_File.txt') as fileToRead:
    with open('4_Task_File_Output.txt', 'w') as fileToWrite:
        for line in fileToRead:
            line = str_converter(line, arr)
            fileToWrite.write(line)
