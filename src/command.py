#encoding:gb2312

'''
����ģʽ
��������ֻҪ���ӻ���ټ̳�Command���࣬�����޸������࣬ʵ�ֵ����
'''

class Command(object):
    def __init__(self):
        pass
    def doCmd(self):
        pass
    
class Move(Command):
    def __init__(self):
        self.status='i am moving'
        
    def doCmd(self):
        print('doCmd move')
class Run(Command):
    def __init__(self):
        self.status='i am running'
        pass
    def doCmd(self):
        print('doCmd run')
#ֻҪ����һ��Eat��������һ��eat����        
class Eat(Command):
    def __init__(self):
        self.status='i am Eating'
        pass
    def doCmd(self):
        print('doCmd eat')
        
        
        
class Player(object):#invoker
    def __init__(self):
        pass
    def command(self,command):
        return command

class Charactor(): #receiver
    def __init__(self):
        self.status=''
        pass
    def getCmd(self,cmd):
        self.cmd=cmd
        self.status=cmd.status
    def doCmd(self):
        self.cmd.doCmd()
        print(self.status)
        
    
p=Player()
c=Charactor()
cmd=p.command(Eat())
c.getCmd(cmd)
c.doCmd()
