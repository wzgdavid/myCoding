# -*- coding:gb2312 -*-


'''
��Ϸ�еĽ�ɫ������״̬
normal  ����
death   ����
poisoned  �ж�
ֻ������״̬�ܱ�����ж�״̬�ܽⶾ

'''

class CharacterStatus(object):
    
    def __init__(self):
        pass
    def beKilled(self):
        pass
    def beRevived(self):
        pass
    def bePoisoned(self):
        pass
    def restoreFromPoison (self):
        pass
        
class Normal(CharacterStatus):  
    def __init__(self):
        pass    
    def beKilled(self):
        print('the human is killed') 
    def beRevived(self):
        pass
    def bePoisoned(self):
        print('the human is poisoned')
    def restoreFromPoison (self):
        pass


class Death(CharacterStatus):  
    def __init__(self):
        pass    
        
    def beKilled(self):
        pass  
        
    def beRevived(self):
        print('the human is revived')
       
    def bePoisoned(self):
        pass
    
    def restoreFromPoison (self):
        pass


class Poisoned(CharacterStatus):
    def __init__(self):
        pass    
        
    def beKilled(self):
        print('the human is killed') 
        
    def beRevived(self):
        pass 
       
    def bePoisoned(self):
        pass
    
    def restoreFromPoison (self):
        print('the human is restored From Poison')
        
    
    
    
class Human():
    def setStatus(self,status):
        self.status=status
        
    def getStatus(self):
        return self.status
    
    def beKilled(self):
        self.status.beKilled()
        self.setStatus(Death())
        
    def beRevived(self):
        self.status.beRevived()
        self.setStatus(Normal())
        
    def bePoisoned(self):
        self.status.bePoisoned()
        self.setStatus(Poisoned())
        
    def restoreFromPoison (self):
        self.status.restoreFromPoison()
        self.setStatus(Normal())
        
        
a=Human() 
a.setStatus(Normal()) 
a.beKilled()
a.beRevived()
a.bePoisoned()

print(a.status)

