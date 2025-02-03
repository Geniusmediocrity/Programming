class House():
    '''описание дома'''
    def __init__(self, street, number):
        '''свойства дома'''
        self.street = street
        self.number = number
        self.age = 4
    
    def build(self):
        '''строит дом'''
        print(f'Дом на улице {self.street} под номером {self.number} -- построен')
        
    def buildings_age(self, year:int):
        '''возраст дома'''
        print(f'Дому {2025 - year}')
    
    
class ProspectHouse(House):
    '''описание домов на проспекте'''
    def __init__(self, prospect, number):
        super().__init__(self, number)
        self.prospect = prospect
        
prospect_house = ProspectHouse("Просрект Пушкина", 99)
print(prospect_house.number)