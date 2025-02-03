n1 = float (input('Введите первое число '))
n2 = float (input('Введите первое число '))
n3 = float (input('Введите первое число '))
if n2 > n1 < n3 :
    min = n1
elif n3 > n2 < n1 :
    min = n2
elif n2 > n3 < n1 :
    min = n3
else:
    print ('числа одинаковы')
if n2 < n1 > n3 :
    max = n1
elif n3 < n2 > n1 :
    max = n2
elif n2 < n3 > n1 :
    max = n3
else:
    pass
print(float(max + min), 'является суммой наибольшего и наименьшего числа')



