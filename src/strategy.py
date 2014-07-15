class Person:
    money=10000
    def __init__(self):
        pass
    
    def travel(self):
        self.travelStrategy.travel()
     
    def setTravelStrategy(self,travelStrategy):
        self.travelStrategy=travelStrategy
        if 'cost' in dir(self.travelStrategy):
            self.money-=self.travelStrategy.cost
        


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
    def __init__(self,cost):
        self.cost=cost
 
    def travel(self):
        print('TravelBy Airline A')

class AirlineB(TravelByPlane):
    def __init__(self,cost):
        self.cost=cost
 
    def travel(self):
        print('TravelBy Airline A')


p=Person()
p.setTravelStrategy(TravelByShip())
p.travel()
p.setTravelStrategy(AirlineB(1500))
p.travel()
print(p.money)