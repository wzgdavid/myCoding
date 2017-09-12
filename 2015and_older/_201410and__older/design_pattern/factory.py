# encoding: utf-8

class Vehicle:
    def __init__(self):
        print('vehicle __init__')

    def move(self):
        print('vehicle can move')


class Car(Vehicle):
    def __init__(self):
        print('Car __init__')

    def move(self):
        print('car can move')


class Truck(Vehicle):
    def __init__(self):
        print('Truck __init__')

    def move(self):
        print('Truck can move')


class VechicleFactory:
    def createVechicle(self):
        return Vehicle()


class CarFactory(VechicleFactory):
    def createVechicle(self):
        return Car()


class TruckFactory(VechicleFactory):
    def createVechicle(self):
        return Truck()


car = CarFactory().createVechicle()
car.move()
t = TruckFactory().createVechicle()
t.move()
