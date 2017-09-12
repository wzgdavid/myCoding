# encoding: utf-8

'''
职责链模式
个人理解，就是把if  else  中不同的处理交给不同的类来处理，
而且这些类又能相互传递消息，但职责链也不光是排他的，也比if else 灵活
说道 if else 我想到了工厂
但工厂模式中平行的类之间不需要传递消息
'''

'''
比如我是一个店员，对于8月份特地商品，我有不同的看法，向店长表达了我的看法，
店长在开会时向经理提出了这个建议，经过简单商讨后，决定这么做，并告知了工厂长
当然 这只是一条可能路径
'''


class Request:
    def __init__(self, suggestion):
        self.suggestion = suggestion

    def __str__(self):
        return self.suggestion


class CORNode(object):
    def __init__(self):
        self.request
        self.successor

    def setRequest(self, request):
        pass

    def setSuccessor(self, node):
        pass


class Clerk(CORNode):
    def __init__(self):
        pass

    def setRequest(self, request):
        self.request = request

    def setSuccessor(self, node):
        self.successor = node
        self.successor.getRequest(self.request)

    def getRequest(self, request):
        self.request = request


class ShopManager(CORNode):
    def __init__(self):
        pass

    def setRequest(self, request):
        self.request = request

    def setSuccessor(self, node):
        self.successor = node
        self.successor.getRequest(self.request)

    def getRequest(self, request):
        self.request = request


class Manager(CORNode):
    def __init__(self):
        pass

    def setRequest(self, request):
        self.request = request

    def setSuccessor(self, node):
        self.successor = node
        self.successor.getRequest(self.request)

    def getRequest(self, request):
        self.request = request


class FactoryManager(CORNode):
    def __init__(self):
        pass

    def setRequest(self, request):
        self.request = request

    def setSuccessor(self, node):
        self.successor = node
        self.successor.getRequest(self.request)

    def getRequest(self, request):
        self.request = request

    def do(self):
        print('修改下月生产计划')


r = Request('下月特定商品提议')
c = Clerk()
sm = ShopManager()
m = Manager()
fm = FactoryManager()
c.setRequest(r)
c.setSuccessor(sm)
sm.setSuccessor(m)
m.setSuccessor(fm)
fm.do()
