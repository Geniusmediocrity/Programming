stroka = int (input ('Введите натуральное число '))
spisok = [i**2 for i in range(1,stroka) if i%5==0 and i%2==0 ]
print (spisok)