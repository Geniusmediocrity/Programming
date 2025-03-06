a =(input(''))
b=0
for i in a[0:3]:
    b +=int(i)
c=0
for j in a[-3:]:
    c += int(j)
if c == b:
    print('Счастливый')
else :
    print ('Не счастливый')