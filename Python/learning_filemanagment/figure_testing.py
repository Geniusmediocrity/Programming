import figure

# Вычисление площади и периметра круга
circle_radius = 5
circle_area = figure.circle_area(circle_radius)
circle_perimeter = figure.circle_perimeter(circle_radius)
print(f"{circle_area = }")
print(f"{circle_perimeter = }")
print()

# Вычисление площади и периметра треугольника
triangle_side1 = 4
triangle_side2 = 3
triangle_side3 = 5
triangle_area = figure.triangle_area(triangle_side1, triangle_side2, triangle_side3)
triangle_perimeter = figure.triangle_perimeter(3, 4, 5)
print(f"{triangle_area = }")
print(f"{triangle_perimeter = }")
print()

# Вычисление площади и периметра прямоугольника
rectangle_length = 6
rectangle_width = 8
rectangle_area = figure.rectangle_area(rectangle_length, rectangle_width)
rectangle_perimeter = figure.rectangle_perimeter(rectangle_length, rectangle_width)
print(f"{rectangle_area = }")
print(f"{rectangle_perimeter = }")
print()

print("Constants: ")
print(f"{figure.e = }")
print(f"{figure.pi = }")