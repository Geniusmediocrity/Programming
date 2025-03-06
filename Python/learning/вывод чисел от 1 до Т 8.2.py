t = int(input('Введите число'))
i=0
for i in range (1,t+1):
    if t >= 35:
        if i == 7:
            continue
        elif i == 13:
            continue
        elif i == 21:
            continue
        elif i == 29:
            continue
        else:
            print(i)
