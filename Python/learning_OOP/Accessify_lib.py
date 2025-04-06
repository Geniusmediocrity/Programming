from accessify import protected, private


class Car:

    @protected
    def start_engine(self):
        return 'Engine sound.'
    
    @private
    def __go(self):
        return "Cars is going!"


class Tesla(Car):

    def run(self):
        return self.start_engine()



tesla = Tesla()

assert 'Engine sound.' == tesla.run()
print(tesla.run())


class Student:
    def __init__(self, name):
        self.name = name
        self._course = 1
        self.__marks = []


student = Student(name="Kevin")
student.__dict__['__marks'] = [5, 4]
print(student.__marks)


class Student:
    def __init__(self, name):
        self.name = name
        self._course = 1
        self.__marks = []


student = Student(name="Kevin")
student.__dict__['__marks'] = [5, 4]
print(student._Student__marks)
#? Во время прямой записи в словарь __dict__ ключа __marks 
#? не срабатывает функциональность приватного модификатора доступа, 
#? который сохраняет атрибут с припиской названия класса. 
#? Поэтому в данной ситуации создается совершенно новый отдельный ключ __marks.
#? А _Student__marks, созданный в инициализации, остается неизменным