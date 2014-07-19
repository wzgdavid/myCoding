# -*- coding:gb2312 -*-
'''
装饰模式

'''
class Car:
    def __init__(self,cid):
        self.cid=cid
        self.color=''
        self.type=''
    def __str__(self):
        return str((self.cid,self.color,self.type))
    


class CarDecorator(object):
    def __init__(self,car):
        self.car=car

class ColorDecorator(CarDecorator):
    colorList=['red','yellow','black']
    def decorate(self):
        pass
    
class ColorRed(ColorDecorator):
    def decorate(self):
        self.car.color=self.colorList[0]
class ColorYellow(ColorDecorator):
    def decorate(self):
        self.car.color=self.colorList[1]
class ColorBlack(ColorDecorator):
    def decorate(self):
        self.car.color=self.colorList[2]
          
        
class TypeDecorator(CarDecorator):
    typeList=['911','cayman','Macan']
    def decorate(self):
        pass
    
class Type911(TypeDecorator):
    def decorate(self):
        self.car.type=self.typeList[0]
class TypeCayman(TypeDecorator):
    def decorate(self):
        self.car.color=self.typeList[1]
class TypeMacan(TypeDecorator):
    def decorate(self):
        self.car.color=self.typeList[2]

cars=[]

'''
3个循环模拟3个流水线
'''

[cars.append(Car(n)) for n in range(100)]

[ColorRed(car).decorate() for car in cars]

[Type911(car).decorate() for car in cars]

[print(car) for car in cars]
    
    


