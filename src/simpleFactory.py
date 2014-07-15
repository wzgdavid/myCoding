class Vehicle:
    def __init__(self):
        pass

class Car(Vehicle):
    def __init__(self):
        self.type='car'
        self.description='Or at least , not car tires'

class Truck (Vehicle):
    def __init__(self):
        self.type='truck'
        self.description='Or when a truck hits a piloted car?'


class Jeep(Vehicle):
    def __init__(self):
        self.type='jeep'
        self.description='Chrysler even produced a commemorative version of its jeep.'

class VehicleFactory:
    def createVehicle(self,carType):
        if carType=='car':
            return Car()
        if carType=='truck':
            return Truck()
        if carType=='jeep':
            return Jeep()
        
vf=VehicleFactory()
v=vf.createVehicle('jeep')
print(v.type,v.description)
