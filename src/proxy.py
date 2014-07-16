# -*- coding:gb2312 -*-
'''
Proxy����RealObject���󣬵�����realObject�ķ���ʱ�ٲ��������
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
            self.real = realObjectDict[self.proxyObject]()#�������ʵ��  
    '''
                ���÷�����ʱ����ʵ����������Ķ���
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
ro=pro.request()#�������ʵ��  
ro.show()


roo=RealObject()#�������ʵ��  
roo.request()
roo.show()





        