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
    def __init__(self,proxyObject):
        self.proxyObject=proxyObject
        
    '''    
    def getObject(self):
        #if 'real' not in dir(self):#避免重复实例化
        if not hasattr(self,'real'):   
            realObjectDict={'ro':RealObject,'ro2':RealObject2}
            if self.proxyObject in realObjectDict.keys():
                self.real = realObjectDict[self.proxyObject]()#这里产生实例  
    '''
        
    def request(self):
        
        self.proxyObject.request()
        return self.proxyObject
    
    def show(self):
        
        self.proxyObject.show()
        return self.proxyObject


#不用代理
ro=RealObject()#这里产生实例  
ro.show()
ro.request()

#用代理
ro2=RealObject()
pro=Proxy(ro2)
pro.show()#这里产生实例  
pro.request()





