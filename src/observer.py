# -*- coding:gb2312 -*-

'''
������⣬��Ϊ�۲������۲�Ķ�����ĳ����Ϊ���ı�۲��ߵ�ĳЩ״̬
�������Ŷӵȴ��кţ����е��������status��waiting��Ϊhandling
���۲�����DisplayBoard���۲�����Person

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