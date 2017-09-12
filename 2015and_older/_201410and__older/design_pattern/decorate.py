# encoding: utf-8


class Car:
    def __init__(self, name):
        self.name = name
        pass

    def __str__(self):
        description = {'car name': self.name}
        if 'color' in dir(self):
            description['color'] = self.color
        if 'ctype' in dir(self):
            description['ctype'] = self.ctype
        return str(description)


class CarDecorator():
    def __init__(self):
        pass

    def setCar(self, car):
        self.car = car

    def color(self, color):
        colors = {'red', 'white', 'black', 'yellow'}
        if color in colors:
            self.car.color = color
        else:
            self.car.color = 'custom color '.join(color)
        return self

    def carType(self, ctype):
        ctypes = {'911', 'Cayman', 'Macan'}
        if ctype in ctypes:
            self.car.ctype = ctype
        else:
            self.car.ctype = 'custom type '.join(ctype)
        return self


car = Car('my car')
car2 = Car('big car')
cd = CarDecorator()
cd.setCar(car)
cd.color('red').carType('911')
cd.setCar(car2)
cd.color('black').carType('F1')
print(car, car2)
