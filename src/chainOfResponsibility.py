#encoding:gb2312

'''
ְ����ģʽ
������⣬���ǰ�if  else  �в�ͬ�Ĵ�������ͬ����������
������Щ�������໥������Ϣ����ְ����Ҳ�����������ģ�Ҳ��if else ���
˵�� if else ���뵽�˹���
������ģʽ��ƽ�е���֮�䲻��Ҫ������Ϣ
'''

'''
��������һ����Ա������8�·��ص���Ʒ�����в�ͬ�Ŀ�������곤������ҵĿ�����
�곤�ڿ���ʱ���������������飬���������ֺ󣬾�����ô��������֪�˹�����

��Ȼ ��ֻ��һ������·��
'''

class Request:
    def __init__(self,suggestion):
        self.suggestion = suggestion
    def __str__(self):
        return self.suggestion 

class CORNode(object):
    def __init__(self):
        self.request
        self.successor
    def setRequest(self,request):
        pass
    def setSuccessor(self,node):
        pass

class Clerk(CORNode):
    def __init__(self):
        pass
    def setRequest(self,request):
        self.request=request
    
    def setSuccessor(self,node):
        self.successor=node
        self.successor.getRequest(self.request)
    def getRequest(self,request):
        self.request=request
        
    
    
class ShopManager(CORNode):
    def __init__(self):
        
        pass
    def setRequest(self,request):
        self.request=request
    
    def setSuccessor(self,node):
        self.successor=node
        self.successor.getRequest(self.request)
    def getRequest(self,request):
        self.request=request 
        
        
class Manager(CORNode):
    def __init__(self):
        
        pass
    def setRequest(self,request):
        self.request=request
    
    def setSuccessor(self,node):
        self.successor=node
        self.successor.getRequest(self.request)
    def getRequest(self,request):
        self.request=request
        
class FactoryManager(CORNode):
    def __init__(self):
        
        pass
    def setRequest(self,request):
        self.request=request
    
    def setSuccessor(self,node):
        self.successor=node
        self.successor.getRequest(self.request)
    def getRequest(self,request):
        self.request=request
    def do(self):
        print('�޸����������ƻ�')
        


       
r=Request('�����ض���Ʒ����')  

c=Clerk()
sm=ShopManager()
m=Manager()
fm=FactoryManager()
c.setRequest(r)
c.setSuccessor(sm)
sm.setSuccessor(m)
m.setSuccessor(fm)
fm.do()














