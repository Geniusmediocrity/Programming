def calculate_area(side_1: float, side_2: float, side_3: float) -> float:
    half_per = (side_1 + side_2 + side_3) / 2
    return (half_per * (half_per - side_1) * (half_per - side_2) * (half_per - side_3)) ** 0.5

def calculate_area_foot_height(footing: float, height: float) -> int | float:
    return footing * height * 0.5

def calculate_gerons_area(side_1: float, side_2: float, side_3: float) -> float:
    half_per = (side_1 + side_2 + side_3) / 2
    return (half_per * (half_per - side_1) * (half_per - side_2) * (half_per - side_3)) ** 0.5

def calculate_area_inscribed_circle(radius: float, side_1: float, side_2: float, side_3: float) -> float:
    return (side_2 * side_1 * side_3) / (4 * radius)

def calculate_area_circumscribed_circle_per(radius: float, perimetr: float) -> float:
    return radius * perimetr

def calculate_area_circumscribed_circle_sides(radius: float, side_1: float, side_2: float, side_3: float) -> float:
    return radius * (side_1 * side_2 * side_3)