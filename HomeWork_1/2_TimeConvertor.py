seconds = int(input('Введите колличество секунд:'))
ss = seconds % 60
mm = (seconds // 60) % 60
hh = seconds // 3600
print(f'{hh}:{mm}:{ss}')
