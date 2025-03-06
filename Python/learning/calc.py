number1 = input('Write first number ')
number2 = input('Write second number ')
variable = input('Write variable ')
if variable == '+':
    print('answer is ', float(number1) + float(number2))
elif variable == '-':
    print ('answer is ', float (number1) - float(number2) )
elif variable == '*':
    print ('answer is ', float(number1) * float(number2) )
elif variable == '/':
    print ('answer is ', float (number1) / float(number2) )
elif variable == '**':
    print ('answer is ', float(number1) ** float(number2) )
elif variable == '%':
    print ('answer is ', float(number1) % float(number2) )
# % - # % - остаток от деления
elif variable == '//':
    print ('answer is ', float (number1) // float(number2) )
#// - это целочисленное деление
else :
    print ('idi v zopy')