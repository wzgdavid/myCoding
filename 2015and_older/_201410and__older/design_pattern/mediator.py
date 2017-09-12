# encoding: utf-8

'''
中介者模式模式
'''
'''
buyer 到两个seller那买商品
'''


class Goods(object):
    def __init__(self):
        self.price = 10

    def __str__(self):
        return 'goods'


class Dealer(object):
    def __init__(self):
        self.money = 100

    def __str__(self):
        return str(self.money)


class Buyer(Dealer):
    def __init__(self):
        self.money = 100
        self.assets = []

    def setSeller(self, seller):
        self.seller = seller

    def buy(self, goods, n=1):
        if n is 1:
            self.assets.append(goods)
            self.money -= goods.price
        else:
            for i in range(n):
                self.assets.append(goods)
            self.money -= goods.price*n


class Seller(Dealer):
    def __init__(self):
        self.money = 100
        self.goodsNum = 10

    def setBuyer(self, buyer):
        self.buyer = buyer

    def sell(self, goods, n=1):
        self.goodsNum -= n
        self.money += goods.price*n


class Mediator(object):
    def __init__(self):
        self.money = 100
        self.goodsNum = 10
        self.assets = []

    def setBuyer(self, buyer):
        self.buyer = buyer

    def setSeller(self, seller):
        self.seller = seller

    def dealwithSeller(self, goods, n=1):
        self.seller.goodsNum -= n
        self.seller.money += goods.price*n

    def dealwithBuyer(self, goods, n=1):
        if n is 1:
            self.buyer.assets.append(goods)
            self.buyer.money -= goods.price
        else:
            for i in range(n):
                self.buyer.assets.append(goods)
            self.buyer.money -= goods.price*n


'''
模拟两次交易
'''
goods = Goods()
goods2 = Goods()
b = Buyer()
s = Seller()
s2 = Seller()
m = Mediator()

m.setBuyer(b)
m.setSeller(s)
m.dealwithBuyer(goods, 2)
m.dealwithSeller(goods, 2)

m.setSeller(s2)
m.dealwithBuyer(goods2)
m.dealwithSeller(goods)

print(b, s, s2)
