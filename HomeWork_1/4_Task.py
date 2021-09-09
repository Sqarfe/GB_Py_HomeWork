numb = int(input('Ведите целое, положительное число:'))
ans = 0
i = 10
while True:
    cur = (numb % i) // (i/10)
    if cur > ans:
        ans = cur
    if i > numb:
        break
    i = i * 10
print(f'{int(ans)}')
