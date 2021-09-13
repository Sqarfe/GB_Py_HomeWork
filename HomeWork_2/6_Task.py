myList = []
myListDict={'название':[], 'цена':[], 'количество':[], 'ед':set()}

myMap = {'название': 'Кофе, 250 гр.', 'цена': '500', 'количество': '20', 'ед': 'шт.'}
myTup = (1, myMap)
myList.append(myTup)
myMap = {'название': 'Сахар', 'цена': '50', 'количество': '100', 'ед': 'кг.'}
myTup = (2, myMap)
myList.append(myTup)
myMap = {'название': 'Чай, 100 гр.', 'цена': '200', 'количество': '31', 'ед': 'шт.'}
myTup = (3, myMap)
myList.append(myTup)

for item in myListDict.values():
    item.clear()
for item in myList:
    myListDict['название'].append(item[1].get('название'))
    myListDict['цена'].append(item[1].get('цена'))
    myListDict['количество'].append(item[1].get('количество'))
    myListDict['ед'].add(item[1].get('ед'))

while True:
    print('Меню:')
    print('Введите 1 для добавления товара')
    print('Введите 2 для удаления товара')
    print('Введите 3 что бы вывести список всхе товаров')
    print('Введите 4 что бы вывести аналитику товаров')

    inp = input()
    if inp == '':
        break

    if not (inp.isdigit()):
        print('!!Некорректный ввод!!')
        continue

    inpInt = int(inp)
    if inpInt < 1 and inpInt > 4:
        print('!!Некорректный ввод!!')
        continue

    if inpInt == 1 :
        id = input('Введите НОМЕР товара: ')
        name = input('Введите ИМЯ товара: ')
        cost = input('Введите ЦЕНУ товара: ')
        quantity = input('Введите КОЛЛИЧЕСТВО товара: ')
        unit = input('Введите ЕД. ИЗМЕРЕНИЯ товара: ')

        if (id.isdigit() and cost.isdigit() and quantity.isdigit()):
            idInt = int(id)
            costInt = int(cost)
            quantityInt = int(quantity)
            if (costInt >= 0 and quantityInt >= 0):
                isIdUsed = False
                for item in myList:
                    if idInt in item:
                        isIdUsed = True
                if isIdUsed:
                    print('Товар с таким id уже существует!')
                    continue

                myMap = {'название': name, 'цена': costInt, 'количество': quantityInt, 'eд': unit}
                myTup = (idInt, myMap)
                myList.append(myTup)

                for item in myListDict.values():
                    item.clear()
                for item in myList:
                    myListDict['название'].append(item[1].get('название'))
                    myListDict['цена'].append(item[1].get('цена'))
                    myListDict['количество'].append(item[1].get('количество'))
                    myListDict['ед'].add(item[1].get('ед'))
                continue1
        print('Что-то пошло не так, повторите попытку.')

    if inpInt == 2 :
        id = input('Введите НОМЕР товара: ')
        if id.isdigit():
            idInt = int(id)
            isRomoved = False
            for item in myList:
                if idInt in item:
                    myList.remove(item)
                    print(f'Товар с id {idInt} был удалён')
                    isRomoved = True

                    for item in myListDict.values():
                        item.clear()
                    for item in myList:
                        myListDict['название'].append(item[1].get('название'))
                        myListDict['цена'].append(item[1].get('цена'))
                        myListDict['количество'].append(item[1].get('количество'))
                        myListDict['ед'].add(item[1].get('ед'))
                    break
            if not isRomoved:
                print(f'Товар с id {idInt} не был найден.')
        else:
            print('Что-то пошло не так, повторите попытку.')
    if inpInt == 3 :
        for item in myList:
            print(item)
    if inpInt == 4 :
        charact = input('Введите характеристику товара: ')
        if charact == 'название' :
            print(myListDict['название'])
        elif charact == 'цена' :
            print(myListDict['цена'])
        elif charact == 'количество' :
            print(myListDict['количество'])
        elif charact == 'ед' :
            print(myListDict['ед'])
        else:
            print('Неправильная характеристика.')




    print()
    print()