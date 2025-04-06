class Point:
    
    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def get_distance_to_origin(self):
        if hasattr(self, "x") and hasattr(self, "y"):
            return (self.x ** 2 + self.y ** 2) ** 0.5
        
    def get_distance(self, point):
        if not isinstance(point, Point):
            print("Передана не точка")
        elif hasattr(self, "x") and hasattr(self, "y") and hasattr(point, "x") and hasattr(point, "y"):
            print(abs(((self.x) ** 2 - (point.x) ** 2) + ((self.y) ** 2 - (point.y) ** 2)) ** 0.5)
        else:
            print("Координаты не заданы")
        
    def display(self):
        if hasattr(self, "x") and hasattr(self, "y"):
            print(f"Point({self.x}, {self.y})")
        else:
            print("Координаты не заданы")
