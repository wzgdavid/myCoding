# -*- coding:gb2312 -*-


'''
��Ϸ�еĽ�ɫ������״̬
normal  ����
death   ����
poisoned  �ж�
ֻ������״̬�ܱ�����ж�״̬�ܽⶾ

'''

class Character(object):
    STATUS_NORMAL=1
    STATUS_DEATH=2
    STATUS_POISONED=3
    
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
        
        
        
class Human(Character):
    def __init__(self,status):
        self.status=status
        pass
    
    def beRevived(self):
        if self.status==Character.STATUS_NORMAL:
            print('can not be revived')
        elif self.status==Character.STATUS_DEATH:
            self.status=Character.STATUS_NORMAL
            print('the human is revived')
            
        elif self.status==Character.STATUS_POISONED:
            print('can not be revived')
        
        
    def restoreFromPoison (self):
        if self.status==Character.STATUS_NORMAL:
            print('can not be revived')
        elif self.status==Character.STATUS_DEATH:
            print('can not be revived')
        elif self.status==Character.STATUS_POISONED:
            self.status=Character.STATUS_NORMAL
            print('the human is restored from poison')
        
        

h=Human(Character.STATUS_DEATH)
h.beRevived()
h.restoreFromPoison()
    
    

