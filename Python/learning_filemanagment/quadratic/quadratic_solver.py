from math import sqrt


def solve_quadratic_equation(a, b, c):
    D = b**2 - (4 * a * c)
    if D < 0:
        return "Корни не существуют"
    x1 = (-b + sqrt(b**2 - 4*a*c)) / (2*a)
    x2 = (-b - sqrt(b**2 - 4*a*c)) / (2*a)
    return x1, x2