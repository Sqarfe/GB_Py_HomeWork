def int_func(txt):
    if len(txt) > 0:
        if len((set(txt) - set('qwertyuiopasdfghjklzxcvbnm'))) == 0:
            return txt.title()


inp = input('Введите слова через пробел: ')
outp = ''
for item in inp.split():
    try:
        outp += int_func(item) + ' '
    except:
        pass

print(outp)