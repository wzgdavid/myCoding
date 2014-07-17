# -*- coding:gb2312 -*-
'''
外观模式
个人理解：和模板方法差不多，视角不同，这里是从这个过程来定义

'''



class Getup():
    def getUp(self):
        print('getUp')
    
    
class BrushTeeth():
    def brushTeeth(self):
        print('brushTeeth')
     
     
class Dress():
    def dress(self):
        print('dress')
        
        
class GoOut():
    def goOut(self):
        print('goOut')

class HaveBreakfast():
    def haveBreakfast(self):
        print('haveBreakfast')
        
        
class ArriveSchool():
    def arriveSchool(self):
        print('ArriveSchool')
    
    
class GoToSchool:
    def __init__(self):
        self.getUp=Getup()
        self.brushTeeth=BrushTeeth()
        self.dress=Dress()
        self.goOut=GoOut()
        self.haveBreakfast=HaveBreakfast()
        self.arraveSchool=ArriveSchool()
        
    def process1(self):
        self.getUp.getUp()
        self.brushTeeth.brushTeeth()
        self.dress.dress()
        self.goOut.goOut()
        self.haveBreakfast.haveBreakfast()
        self.arraveSchool.arriveSchool()
        
    def process2(self):
        self.getUp.getUp()
        self.dress.dress()
        self.brushTeeth.brushTeeth()
        self.haveBreakfast.haveBreakfast()
        self.goOut.goOut()
        self.arraveSchool.arriveSchool()
       

'''
上学前一系列动作作为参数传给Student的方法
'''        
class Student:
    def goToSchool(self,processOfgts):
        self.gts=processOfgts
        self.gts()
        pass
    
    
g=GoToSchool()
s=Student()
s.goToSchool(g.process2)      

        