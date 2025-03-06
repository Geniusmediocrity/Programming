f_number = list(input('Ведите 10 целых чисел '))
if len(f_number) < 10 :
    f_number += ''
c = 0
def a (nn):
    global f_number
    global c
    for r in f_number:
        if int(r) < 5 :
            f_number.remove(r)
        else :
            c += int(r)
    return c
print (a(c))