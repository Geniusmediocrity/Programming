n = int(input('Напишите число'))
a = 0
for s in range (0, n+1):
    if s % 2 ==0:
        a+=s
print ('сумма равна =', a)