# encoding: utf-8


class Vehicle:
    def __init__(self):
        pass


class VehicleType:
    CAR = 'car'
    TRUCK = 'truck'
    JEEP = 'jeep'


class Car(Vehicle):
    def __init__(self):
        self.type = VehicleType.CAR
        self.description = ' Or at least , not car tires'


class Truck (Vehicle):
    def __init__(self):
        self.type = VehicleType.TRUCK
        self.description = ' Or when a truck hits a piloted car?'


class Jeep(Vehicle):
    def __init__(self):
        self.type = VehicleType.JEEP
        self.description = ' Chrysler jeep.'


class VehicleFactory:
    def createVehicle(self, vtype):
        vtypeDict = {VehicleType.CAR: Car,
                     VehicleType.TRUCK: Truck,
                     VehicleType.JEEP: Jeep}
        return vtypeDict[vtype]()


vf = VehicleFactory()
v = vf.createVehicle(VehicleType.JEEP)
print(v.type, v.description)
