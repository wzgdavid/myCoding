# encoding: utf-8

import weakref

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


ro = RealObject()
ro.show()
ro.request()

pro = Proxy(ro)
pro.show()
pro.request()
print(pro)
# 后来发现python库里有代理
pro2 = weakref.proxy(ro)
pro2.show()
pro2.request()
print(pro2)
