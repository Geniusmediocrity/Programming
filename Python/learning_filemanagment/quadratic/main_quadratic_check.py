from quadratic_solver import solve_quadratic_equation


coefficients1 = (1, -3, 2)
coefficients2 = (1, 2, 1)
coefficients3 = (1, 1, 1)

result1 = solve_quadratic_equation(*coefficients1)
result2 = solve_quadratic_equation(*coefficients2)
result3 = solve_quadratic_equation(*coefficients3)

print(f"Уравнение {coefficients1}: Корни = {result1}")
print(f"Уравнение {coefficients2}: Корни = {result2}")
print(f"Уравнение {coefficients3}: Корни = {result3}")