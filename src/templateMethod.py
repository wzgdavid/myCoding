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

    # template 1
    def process1(self):
        print('-------------template 1---------------')
        self.getUp()
        self.dress()
        self.brushTeeth()
        self.haveBreakfast()
        self.goOut()
        self.arriveSchool()

    # template 2
    def process2(self):
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


s = Student()
s.process2()
s.process1()
