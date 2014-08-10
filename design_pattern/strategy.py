# -*- coding:gb2312 -*-
'''
������⡣����ģʽ�������ĳ���������ǹ̶��ģ����ǿ��Խ��������Ĳ������������������ִͬ�в�ͬ�ķ�����ͨ����������Ǹ���
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
# ��ͬ���ԶԵ��������������Ӱ��
p.setTravelStrategy(AirlineB(2500))
p.travel()
print(p.money)
