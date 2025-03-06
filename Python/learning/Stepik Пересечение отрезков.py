''' Проверочный данные
а1,б1,а2,б2

1,5,6,10 #пустое множество  ?!
6,10,1,5 #пустое множество  ?!
1,10,3,5 #3 5    ?!
1,5,3,7 #3 5     ?!
3,7,1,5 #3 5     ?!
3,5,1,10 #3 5    ?!
1,5,5,10 #5      !!
5,10,1,5 #5      !!
1,5,1,5 #1 5     !!
1,5,1,10 #1 5    !!
5,10,1,10 #5 10  !!
1,10,5,10 #5 10  !!
1,10,1,5 #1 5    !!      '''
number_a1,number_b1,number_a2,number_b2 = int(input('')),int(input('')),int(input('')),int(input(''))
if number_a1 > number_b1 or number_a2 > number_b2:
    print ('Перепроверьте данные')
else:
    if number_a1 == number_a2 :                  #от сюда
        if number_b1 < number_b2:
            print (number_a1,number_b1)
        elif number_b1 > number_b2:
            print (number_a1,number_b2)
        elif number_b1 == number_b2:
            print (number_a1,number_b1)
    elif number_b1 == number_b2:
        if number_a1 < number_a2:
            print (number_a2,number_b1)
        elif number_a1 > number_a2:
            print(number_a1,number_b1)
        elif number_a1 == number_a2:
            print (number_a1,number_b1)
    elif number_b1 == number_a2:
        print (number_b1)
    elif number_b2 == number_a1:
        print(number_b2)                     #до сюда решает все вопросы с пересечениями/oбщими точками
    elif number_a2 > number_a1 and number_b2 < number_b1:                          #от сюда
        print(number_a2,number_b2)
    elif number_b1 > number_a2 > number_a1 and number_a2 < number_b1 <number_b2 :
        print(number_a2,number_b1)
    elif number_a2 < number_a1 < number_b2 and number_a1 < number_b2 < number_b1:
        print(number_a1,number_b2)
    elif number_a2 < number_a1 < number_b2 and number_a2 < number_b1 < number_b2:
        print (number_a1,number_b1)
    elif number_a1 < number_a2 < number_b1 and number_a1 < number_b2 < number_b1:
        print(number_a2,number_b2)                                                #до сюда решает несмотря на отсутствие общих точек
    else:
        print('пустое множество')