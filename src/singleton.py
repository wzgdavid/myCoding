#encoding:gb2312

'''
单例模式

'''


class Singleton(object):
    def __new__(self):
        if not hasattr(self,'_instance'):
            self._instance =  super(Singleton, self).__new__(self)
        return self._instance



class FIFAWouldCup(Singleton):
    height='36cm'
    
    

a=FIFAWouldCup()
b=FIFAWouldCup()

print(a is b)