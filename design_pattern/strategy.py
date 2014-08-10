# -*- coding:gb2312 -*-
'''
个人理解。策略模式就是类的某个方法不是固定的，而是可以接受外来的参数，根据这个参数不同执行不同的方法，通常这个参数是个类
'''


class Person:
    money = 10000

    def __init__(self):
        pass

    def travel(self):
        self.travelStrategy.travel()

    def setTravelStrategy(self, travelStrategy):
        self.travelStrategy = travelStrategy
        if 'cost' in dir(self.travelStrategy):
            self.money -= self.travelStrategy.cost


class TravelStrategy():
    def travel(self):
        pass


class TravelByPlane(TravelStrategy):
    def travel(self):
        print('TravelByPlane')


class TravelByShip(TravelStrategy):
    def travel(self):
        print('TravelByShip')


class TravelByTrain(TravelStrategy):
    def travel(self):
        print('TravelByTrain')


class AirlineA(TravelByPlane):
    def __init__(self, cost):
        self.cost = cost

    def travel(self):
        print('TravelBy Airline A')


class AirlineB(TravelByPlane):
    def __init__(self, cost):
        self.cost = cost

    def travel(self):
        print('Travel By Airline B')


p = Person()
p.setTravelStrategy(TravelByShip())
p.travel()
# 不同策略对调用主体的属性有影响
p.setTravelStrategy(AirlineB(2500))
p.travel()
print(p.money)
