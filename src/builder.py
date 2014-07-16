# -*- coding:gb2312 -*-

'''
和factory很像
'''


    
class Car():
    def setBodyColor(self,bColor):
        self.bodyColor=bColor
    def setWheelSize(self,wSize):
        self.wheelSize=wSize

        

class CarBuilder:
    def buildCar(self,bColor,wSize):
        car=Car()
        car.setBodyColor(bColor)
        car.setWheelSize(wSize)
        return car

        
    
class Director:
    def __init__(self):
        self.builder=CarBuilder()
        
    def getCarA(self):
        return self.builder.buildCar('red',90)
    
    def getCarB(self):
        return self.builder.buildCar('yellow',80)
       
  
    
d=Director()
car=d.getCarA()
print(car.bodyColor,car.wheelSize)
    