# -*- coding:gb2312 -*-
'''
个人理解：以一个特定顺序执行一组方法
'''

'''
定义一个早上起床去学校的过程，这是一个接口
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
    每个具体工作还可以结合策略模式
    '''


s = Student()
s.process2()
s.process1()
