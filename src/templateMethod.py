# -*- coding:gb2312 -*-
'''
������⣺��һ���ض�˳��ִ��һ�鷽��
'''

'''
����һ��������ȥѧУ�Ĺ��̣�����һ���ӿ�
'''
class GoToSchool:
    def getUp(self):
        pass
    def dress(self):
        pass
    def haveBreakfast(self):
        pass
    def brushTeeth(self):
        pass
    def goOut(self):
        pass
    def arriveSchool(self):
        pass
    def process1(self):#template 1
        print('-------------template 1---------------')
        self.getUp()
        self.dress()
        self.brushTeeth()
        self.haveBreakfast()
        self.goOut()
        self.arriveSchool()
    def process2(self):#template 2
        print('-------------template 2---------------')
        self.getUp()
        self.brushTeeth()
        self.dress()
        self.goOut()
        self.haveBreakfast()
        self.arriveSchool()
        
class Student(GoToSchool):
    def getUp(self):
        print('getUp')
    def dress(self):
        print('dress')
    def haveBreakfast(self):
        print('haveBreakfast')
    def brushTeeth(self):
        print('brushTeeth')
    def goOut(self):
        print('goOut')
    def arriveSchool(self):
        print('arriveSchool')
    '''
    ÿ�����幤�������Խ�ϲ���ģʽ
    '''

s=Student()
s.process2()
s.process1()