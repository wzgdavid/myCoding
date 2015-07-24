# encoding: utf-8

'''
date: 2015-5-11
'''
class Charactor(object):
    def __init__(self):
        pass


class Human(Charactor):
    def __init__(self):
        print('Human __init__')
    def foo(self):
        print 'human foo'


class Orc(Charactor):
    def __init__(self):
        print('Orc __init__')
    def foo(self):
        print 'orc foo'


class CharactorFactory(object):

    @classmethod
    def create(cls, cls_name):
        '''
        通过字符串参数生成类实例
        '''
        if cls_name.lower() in [n.lower() for n in globals()]:
            #print cls_name.capitalize()
            return globals()[cls_name.capitalize()]()
        else:
            print 'there is no class in the module'


h2 = Human()

human = CharactorFactory.create('human')
print type(human) is type(h2)
orc = CharactorFactory.create('orc')

human.foo()
orc.foo()