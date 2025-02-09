"""Объявите класс Point3D для точек с тремя координатами x, y, z. 
Создайте несколько экземпляров этого класса и через них выведите в консоль значения x,y,z. Далее, сделайте следующие манипуляции:
    
        - поменяйте любое значение координаты в классе Point3D и посмотрите как это повлияет на отображаемые величины экземпляров класса;
        - удалите координату z в классе Point3D и убедитесь, что она будет отсутствовать во всех экземплярах;
        - поменяйте координату в каком-либо экземпляре класса и посмотрите на результат."""
        
class Point3D:
    "CLASS"
    def __init__(self, x_point, y_point, z_point):
        self.x = x_point
        self.y = y_point
        self.z = z_point
        
    
point = Point3D(10, 15, 20)
print(f"before: {getattr(point, "x", False)}, {getattr(point, "y", False)}, {getattr(point, "z", False)}")

setattr(point, "x", 100)
setattr(point, "y", 200)
delattr(point, "z")
print(f"after: {getattr(point, "x")}, {getattr(point, "y", False)}, {getattr(point, "z", False)}")
print(Point3D.__doc__)

print(dir(point))