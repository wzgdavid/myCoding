# encoding: utf-8
'''
和decorate模式一个原理,  
例如组装电脑, 此模式就像品牌机, 出厂就组装好了有固定型号
             decorate 模式就像组装机
'''
class Car():
    def setBodyColor(self, bColor):
        self.bodyColor = bColor

    def setWheelSize(self, wSize):
        self.wheelSize = wSize


class CarBuilder:
    def buildCar(self, bColor, wSize):
        car = Car()
        car.setBodyColor(bColor)
        car.setWheelSize(wSize)
        return car


class Director:
    def __init__(self):
        self.builder = CarBuilder()

    def getCarA(self):
        '''
        型号 A
        '''
        return self.builder.buildCar('red', 90)

    def getCarB(self):
        '''
        型号 B
        '''
        return self.builder.buildCar('yellow', 80)


d = Director()
car = d.getCarA()
print(car.bodyColor, car.wheelSize)
