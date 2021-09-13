inp = input('Введите строку из нескольких слов: ')

lst = inp.split(' ')

for word in lst:
    print(f'{word:.10}')