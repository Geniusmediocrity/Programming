from math import sqrt
number_a, number_b, number_c = float(input()),float(input()),float(input())
discriminant = number_b ** 2 - 4 * number_a * number_c
if discriminant < 0:
    print('Нет корней')
elif discriminant == 0:
    root_x = ( -(number_b) / (2 * number_a) )
    print (root_x)
else:
    root_x1 = ( (-(number_b) - sqrt(discriminant) ) / (2 * number_a) )
    root_x2 = ( (-(number_b) + sqrt(discriminant) ) / (2 * number_a) )
    min_root = min(root_x1,root_x2)
    max_root = max(root_x1,root_x2)
    print(min_root)
    print(max_root)