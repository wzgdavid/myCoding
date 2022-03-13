import random
from collections import Counter
from operator import itemgetter

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
        return self.cards

class TexasHold_em(Cards):
    #num_list = ['2', '3','4','5','6','7','8','9','10','J','Q','K','A']

    def __num(self, card):
        return card[2:]

    def __suit(self, card):
        return card[0]

    def get_random_cards(self, n):
        '''随机得到n张牌'''
        got_cards = []
        for i in range(n):
            card = random.choice(self.cards)

            got_cards.append(card)
            self.cards.remove(card)
        return got_cards

    def get_card(self, card):
        '''获得指定的牌'''
        if card not in self.cards:
            return
        self.cards.remove(card)
        return card

c = Cards()
#print(c.cards)

t = TexasHold_em()
print('player A')
print(t.get_random_cards(2))
print('player B')
print(t.get_random_cards(2))
print('player C')
print(t.get_random_cards(2))

print('public cards')
print(t.get_random_cards(5))