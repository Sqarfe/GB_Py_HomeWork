# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
#   выполнить подсчет количества строк, количества слов в каждой строке.
line_counter = 0

with open('2_Task_File.txt', 'r') as f:
    for line in f:
        print(f'line: {line_counter}, words in line: {len(line.strip().split())}')
        line_counter += 1
