list = []

print('Введите значения, для завершения - введите пустую строку:')

while True :
    inp = input()
    if inp == '':
        break
    list.append(inp)

itr = 1
while itr < len(list) :
    a = list[itr-1]
    list[itr-1] = list[itr]
    list[itr] = a
    itr = itr + 2

for i in list:
    print(i)