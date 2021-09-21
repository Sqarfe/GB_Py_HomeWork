# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
#       название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.


# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.

import json

ProfitableCompany = {}
AllCompany = [{}, {}]
with open('7_Task_File.txt') as file:
    for line in file:
        args = line.split()
        profit = int(args[2]) - int(args[3])
        if profit > 0:
            ProfitableCompany[args[0]] = profit
        AllCompany[0][args[0]] = profit
    ProfitableCompany_Profit = sum(ProfitableCompany.values()) / len(ProfitableCompany)
    AllCompany[1]['average_profit'] = round(sum(AllCompany[0].values()) / len(AllCompany[0]))

    print(f'Прибыльные фирмы: {ProfitableCompany}')
    print(f'Средняя прибыль прибыльных фирм: {ProfitableCompany_Profit}')
    print(f'Все фирмы и их средняя прибыль: {AllCompany}')

with open('7_Task_File_Output.json', 'w') as file:
    json.dump(AllCompany, file)

