# -*- coding:gb2312 -*-
'''
Proxy代理RealObject对象，当调用realObject的方法时再产生其对象，
'''
class Interface :
    def request(self):
        pass
    def show(self):
        pass
    

class RealObject(Interface): 
    def __init__(self):
        print('init RealObject')
    def request(self):
        print ("Real request.")
    def show(self):
        print ("Real show.")

class RealObject2(Interface): 
    def __init__(self):
        print('init RealObject2')
    def request(self):
        print ("RealObject2 request.")
    def show(self):
        print ("RealObject2 show.")
        
        
class Proxy(Interface):
    def __init__(self,whichRealObject):
        self.proxyObject=whichRealObject
        
    def getObject(self):
        realObjectDict={'ro':RealObject,'ro2':RealObject2}
        if self.proxyObject in realObjectDict.keys():
            self.real = realObjectDict[self.proxyObject]()#这里产生实例  
    '''
                调用方法的时候再实例化所代理的对象
    '''
    def request(self):
        self.getObject()
        self.real.request()
        return self.real
    def show(self):
        self.getObject()
        self.real.show()
        return self.real

#yong
pro=Proxy('ro2')
ro=pro.request()#这里产生实例  
ro.show()


roo=RealObject()#这里产生实例  
roo.request()
roo.show()





        