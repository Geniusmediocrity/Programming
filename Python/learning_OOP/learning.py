class Car:
    
    car_count = 0
    def start(self, name, make, model):
        print("engine is started succesfull")
        self.name = name
        self.make = make
        self.model = model
        self.car_count += 1
        print(self.car_count)
    print(car_count)
    
    @staticmethod
    def CARR(clsassmethod):
        print("cARRRR")
    
    
car_a = Car
car_a.start(Car, 111, 333, 444)

car_b = Car
car_b.start(Car, 222, 555, 777)
print(car_a.car_count)

Car.CARR()
Car.start(Car, 10, 10, 10)