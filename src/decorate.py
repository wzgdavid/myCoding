# -*- coding:gb2312 -*-

class Car:
    def __init__(self,name):
        self.name=name
        pass
    
    def __str__(self):
        description={'car name':self.name}
        
        if 'color' in dir(self):
            description['color']=self.color
        if 'ctype' in dir(self):
            description['ctype']=self.ctype  
        return str(description)
    
    
class CarDecorator():
    def __init__(self,car):
        self.car=car
        pass
    
    def color(self,color):
        colors={'red','white','black','yellow'}
        if color in colors:
            #print('color is ',color)
            self.car.color=color
        else:
            #print('custom color')
            self.car.color='custom color '+color
        return self #可以链式调用，就像jQuery
    
    def carType(self,ctype):
        ctypes={'911','Cayman','Macan'}
        if ctype in ctypes:
            #print('car type is ',ctype)
            self.car.ctype=ctype
        else:
            #print('custom type')
            self.car.ctype='custom type '+ctype
        return self
 


           
car=Car('my car')    
cd=CarDecorator(car)
cd.color('red').carType('911')
print(car)