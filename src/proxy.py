# -*- coding:gb2312 -*-
'''
Proxy代理RealObject对象，当调用realObject的方法时再产生其对象，
'''


class Interface:
    def request(self):
        pass

    def show(self):
        pass


class RealObject(Interface):
    def __init__(self):
        print('init RealObject')

    def request(self):
        print("Real request.")

    def show(self):
        print("Real show.")


class RealObject2(Interface):
    def __init__(self):
        print('init RealObject2')

    def request(self):
        print("RealObject2 request.")

    def show(self):
        print("RealObject2 show.")


class Proxy(Interface):
    def __init__(self, whichRealObject):
        self.proxyObject = whichRealObject

    def getObject(self):
        if not hasattr(self, 'real'):
            realObjectDict = {'ro': RealObject, 'ro2': RealObject2}
            if self.proxyObject in realObjectDict.keys():
                # 这里产生实例
                self.real = realObjectDict[self.proxyObject]()

    def request(self):
        self.getObject()
        self.real.request()
        return self.real

    def show(self):
        self.getObject()
        self.real.show()
        return self.real


# 用代理
pro = Proxy('ro2')
ro = pro.show()
pro.request()

# 不用代理
ro = RealObject()
ro.request()
ro.show()
