#encoding:gb2312

'''
桥接模式
和装饰模式有异曲同工之处，都是多维度，但是观察点不同
桥接模式的维度用在实例之间,不同维度实例只要关心自己的工作，
不同实例分工合作，下层为上层提供调用接口（类本身和类方法）


'''

'''
做面包过程
'''


class 成型(object):
    def __init__(self):
        pass
    
class 方形(成型):
    def __init__(self):
        print('方形')
        
class 圆形(成型):
    def __init__(self):
        print('圆形')
        
class 发酵(object):
    def __init__(self,成型实例):
        self.成型完成=成型实例

class 高温发酵(发酵):
  
    def 发酵(self,湿度):
        print('湿度',湿度,'高温发酵')
    
class 低温发酵(发酵):
    
    def 发酵(self,湿度,成型实例):
        print('湿度',湿度,'低温发酵')  
    
class 烘焙():  
    def __init__(self,发酵实例):
        self.发酵完成=发酵实例

class 高温烘焙(烘焙):
    
    def 烘焙(self,风力):
        print('风力',风力,'高温烘焙')
    
class 低温烘焙(烘焙):
    
    def 烘焙(self,风力):
        print('风力',风力,'低温烘焙') 
        

    
  
a=方形()
b=高温发酵(a)
b.发酵('80%')
c=低温烘焙(b)
c.烘焙('三档')
