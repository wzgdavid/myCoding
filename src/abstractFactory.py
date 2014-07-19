#encoding:gb2312


'''
抽象工厂模式


'''


class Charactor(object):
    def __init__(self):
        pass
        

class Human(Charactor):
    def __init__(self):        
        print('Human __init__')
        
class Orc(Charactor):
    def __init__(self):        
        print('Orc __init__')    
        
class CharactorFactory(object):
    def createCharactor(self):
        pass
        
class HumanFactory(CharactorFactory):
    def createCharactor(self):
        return Human()
    
class OrcFactory(CharactorFactory):
    def createCharactor(self):
        return Orc()
    
hf=HumanFactory()
h=hf.createCharactor()
of=OrcFactory()
o=of.createCharactor()
        
        
        