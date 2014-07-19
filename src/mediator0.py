# encoding:gb2312

'''
中介者模式模式
'''

'''
buyer 到两个seller那买商品
'''
class Goods(object):
    def __init__(self):
        self.price=10
    def __str__(self):
        return 'goods' 

class Dealer(object):
    def __init__(self):
        self.money=100 
    def __str__(self):
        return str(self.money) 
    
          
class Buyer(Dealer):
    def __init__(self):
        self.money=100
        self.assets=[]
        
    
    def setSeller(self,seller):
        self.seller=seller
    
    def buy(self,something,n=1):
        if n is 1:
            self.assets.append(something)
            self.money-=something.price
        else:
            for i in range(n):
                self.assets.append(something)
            self.money-=something.price*n
 
    
class Seller(Dealer):
    def __init__(self):
        self.money=100
        self.goodsNum=10
        pass
    def setBuyer(self,buyer):
        self.buyer=buyer
        
    def sell(self,goods,n=1):
        self.goodsNum-=n
        self.money+=goods.price*n
        
        
'''
模拟两次交易
'''        
goods=Goods()
goods2=Goods()
b=Buyer()
s=Seller()
s2=Seller()

b.setSeller(s)
b.buy(goods,2)
s.setBuyer(b)
s.sell(goods,2)

b.setSeller(s2)
b.buy(goods2)
s2.setBuyer(b)
s2.sell(goods2)
print(b,s,s2)

