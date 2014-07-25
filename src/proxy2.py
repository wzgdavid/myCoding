# -*- coding:gb2312 -*-
'''
Proxy����RealObject���󣬵�����realObject�ķ���ʱ�ٲ��������
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
    def __init__(self, proxyObject):
        self.proxyObject = proxyObject

    def request(self):

        self.proxyObject.request()
        return self.proxyObject

    def show(self):
        self.proxyObject.show()
        return self.proxyObject


# ���ô���
ro = RealObject()
ro.show()
ro.request()

# �ô���
ro2 = RealObject()
pro = Proxy(ro2)
pro.show()
pro.request()
