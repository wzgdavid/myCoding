# encoding: utf-8

class Cards(object):
    '''一副牌'''
    def __init__(self):
        self.cards = []
        self.create_cards()

    def create_cards(self):
        # suit: 花色(s-spades黑桃 h-hearts红桃 d-diamonds方块 c-clubs梅花)
        suits = ['s', 'h', 'd', 'c']
        num = [str(n) for n in range(2, 11)]
        num.extend(['J', 'Q', 'K', 'A'])
        self.num_list = num
        self.cards = []
        self.obj_cards = []
        for s in suits:
            for n in num:
                self.cards.append(s+'_'+n)
                self.obj_cards.append(Card(s, n))

class Card(object):
    '''一张牌'''
    def __init__(self, suit, num):
        self.suit = suit
        self.num = num
        #self.card = self.__card_str()

    #def __card_str(self):
