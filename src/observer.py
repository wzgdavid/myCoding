# -*- coding:gb2312 -*-

'''
个人理解，因为观察者所观察的东西的某个行为而改变观察者的某些状态
在银行排队等待叫号，被叫到号码的人status从waiting变为handling
被观察者是DisplayBoard，观察者是Person

'''
class BeObserved():
    def addObserver(self,observer):
        pass


class DisplayBoard(BeObserved):
    def __init__(self):
        self.observerDict={}
        self.callNumber=0
        
    def addObserver(self,observer):
        #self.observerList.append(observer)
        self.observerDict[observer]=observer.number
    
    def call(self,num):
        self.callNumber=num
        for k,v in self.observerDict.items():
            if self.callNumber==v:
                k.updateStatus('handling')
                
    
class Observer():
    def update(self):
        pass
    
class Person(Observer):
    def __init__(self):
        self.status='waiting'
    
    def setNumber(self,num):
        self.number=num
    
    def updateStatus(self,status):
        self.status=status
        pass
    
    
    
p1=Person()
p2=Person() 
p1.setNumber(123)
p2.setNumber(124)   

db=DisplayBoard()
db.addObserver(p1)
db.addObserver(p2)
db.call(123)

print(p1.number,p1.status)
print(p2.number,p2.status)