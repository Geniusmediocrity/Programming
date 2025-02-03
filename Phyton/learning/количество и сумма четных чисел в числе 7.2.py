number = int (input('Введите число: '))
n_colvo = 0
n_sum = 0
while number :
    if  number % 2 == 0 :
       n_sum += number
       n_colvo += 1
       number -= 2
    else :
        number -= 1

print ('Количество четных цифр: ', n_colvo)
print ('Сумма четных цифр: ', n_sum)

