# encoding: utf-8
from __future__ import division #  python 3 不用
from itertools import combinations

import random
import utils
from cards import Cards
from collections import Counter
from operator import itemgetter

class TexasHold_em(Cards):
    '''
    计算概率
    '''
    #num_list = ['2', '3','4','5','6','7','8','9','10','J','Q','K','A']
    def all_comb(self):
        '''
        所有组合数
        '''
        # n!/[(n-m)!m!] n=52 m=7
        #return fa(52)/(fa(45)*fa(7))
        return 133784560
  
    def func(self, condition):
        cond_dict = {
            'pair': self.__is_pair,
            '3pair': self.__is_3pair,
            'straight': self.__is_straight,
            'normal_straight': self.__is_normal_straight,
            'flush': self.__is_one_suit,
            'normal_flush': self.__is_normal_flush,
            'straight_flush': self.__is_straight_flush,
            'normal': self.__is_normal,
            'single_A': self.__is_single_A
        }
        cnt = 0
        all_patterns = combinations(self.cards, 5)
        for a_hand in all_patterns:
            if cond_dict[condition](a_hand):
                cnt += 1
        return cnt

    def pair(self):
        '''对子数量'''
        #return self.func('pair')
        rtn = utils.C(4, 2)*13*utils.C(12, 5)*(4**5)
        return rtn

    def three_of_a_kind(self):
        '''豹子数量'''
        return self.func('3pair')

    def straight(self):
        ''' 所有顺子'''
        return self.func('straight')

    def normal_straight(self):
        ''' 普通顺子，不带顺金'''
        return self.func('normal_straight')

    def flush(self):
        ''' 所有金花'''
        return self.func('flush')

    def normal_flush(self):
        ''' 普通顺子，不带顺金'''
        return self.func('normal_flush')

    def straight_flush(self):
        '''顺金'''
        return self.func('straight_flush')

    def normal(self):
        '''杂牌'''
        return self.func('normal')

    def single_A(self):
        '''单A'''
        return self.func('single_A')

    def __num(self, card):
        return card[2:]

    def __suit(self, card):
        return card[0]

    def __is_pair(self, t):
        '''参数t为combinations中的一种，即拿到的一手牌'''
        tu = [self.__num(n) for n in t]
        return utils.one_pair(tu)

    def __is_3pair(self, t):
        '''一手牌3张点数相同'''
        return self.__num(t[0]) == self.__num(t[1]) == self.__num(t[2])

    def __is_straight(self, t):
        '''一手牌是否是顺子'''
        index_1 = self.num_list.index(self.__num(t[0]))
        index_2 = self.num_list.index(self.__num(t[1]))
        index_3 = self.num_list.index(self.__num(t[2]))
        index = [index_1, index_2, index_3]
        index.sort()
        if index[2] == index[1]+1 and index[1] == index[0]+1:
            #print index, t
            return True
        if index == [0, 1, 12]:
            return True

    def __is_one_suit(self, t):
        '''是否金花'''
        return self.__suit(t[0]) == self.__suit(t[1]) == self.__suit(t[2])
    
    def __has_A(self, t):
        return self.__num(t[0]) == 'A' or self.__num(t[1]) == 'A' or self.__num(t[2]) == 'A'

    def __is_normal_straight(self, t):
        return self.__is_straight(t) and not self.__is_one_suit(t)
    
    def __is_normal_flush(self, t):
        return self.__is_one_suit(t) and not self.__is_straight(t)

    def __is_straight_flush(self, t):
        return self.__is_straight(t) and self.__is_one_suit(t)

    def __is_normal(self, t):
        return not self.__is_one_suit(t) and not self.__is_straight(t)\
                and not self.__is_pair(t) and not self.__is_3pair(t)

    def __is_single_A(self, t):
        return self.__has_A(t) and self.__is_normal(t)
    
#######################################################################################
#######################################################################################
#######################################################################################
#######################################################################################
#######################################################################################
#######################################################################################

    def get_random_cards(self, n):
        '''
        随机得到n张牌
        '''
        got_cards = []
        for i in range(n):
            card = random.choice(self.cards)

            got_cards.append(card)
            self.cards.remove(card)
        return got_cards

    def public_cards(self):
        return self.get_random_cards(5)

    def my_cards(self):
        return self.get_random_cards(2)

    def shuffle(self):
        '''洗牌'''
        self.create_cards()
    
    #def sort_cards(self, cards):
    #    return sorted(cards, key=itemgetter(2))
    #'''
    #牌型点数（5张牌）比较大小用
    #高牌   ---- 59     点数和
    #对子   116----164  点数和+100
    #两对   215----265  点数和+200
    #三条   300+        点数和+300
    #顺子   400+        点数和+400
    #同花   500+        点数和+500
    #俘虏   600+        点数和+600
    #同花顺  700+
    #皇家同顺 800+
    #'''
    def __has_pair(self, cards):
        '''
        判断7张牌中是否有对子，cards = [1,2,3,4,5,6,7]
        '''
        num_list = []
        [num_list.append(self.__num(card)) for card in cards]
        c = Counter(num_list)

        if c.most_common(1)[0][1] == 2 and c.most_common(2)[1][1] == 1:
            return True
        return False

    def __has_two_pairs(self, cards):

        num_list = []
        [num_list.append(self.__num(card)) for card in cards]
        c = Counter(num_list)

        if c.most_common(1)[0][1] == 2 and c.most_common(2)[1][1] == 2:
            return True
        return False

    def __has_straight(self, cards):
        index_list = []
        for card in cards:
            index_list.append(self.num_list.index(self.__num(card)))
        #sorted_list = sorted(index_list)
        index_list.sort()
        cnt = 0
        for i, item in enumerate(index_list):
            if i == 0:continue
            if index_list[i-1] + 1 == item:
                cnt += 1
            else:
                cnt = 0
        if cnt == 4:
            return True
        else:
            return False

    def __has_flush(self, cards):

        suit_list = []
        [suit_list.append(self.__suit(card)) for card in cards]
        c = Counter(suit_list)
        if c.most_common(1)[0][1] >= 5:
            return True
        return False
        #print c.most_common(1)[0][1]

    def __has_FullHouse(self, cards):
        num_list = []
        [num_list.append(self.__num(card)) for card in cards]
        c = Counter(num_list)

        if c.most_common(2)[0][1] == 3 and c.most_common(2)[1][1] == 2:
            return True
        return False

    def __has_three_ofakind(self, cards):
        num_list = []
        [num_list.append(self.__num(card)) for card in cards]
        c = Counter(num_list)

        if c.most_common(1)[0][1] == 3 and c.most_common(2)[1][1] == 1:
            return True
        return False

    def __has_four_ofakind(self, cards):
        num_list = []
        [num_list.append(self.__num(card)) for card in cards]
        c = Counter(num_list)

        if c.most_common(1)[0][1] == 4:
            return True
        return False

    def test(self):
        cards = self.get_random_cards(7)
        print cards
        print self.__has_straight(cards)
        


if __name__ == '__main__':

    z = TexasHold_em()
    #print z.cards
    for n in range(1000):

        z.test()
        z.shuffle()




    #start = time.time()
    #print z.all_comb()
    #end = time.time()
    #print end - start
    #print z.three_of_a_kind()
    #print z.straight_flush()
    #print z.normal_flush()
    #print z.normal_straight()
    #print z.pair()
    #print z.normal()
    #print z.single_A()
    
    #d = z.pair()+z.normal_straight()+z.normal_flush()+z.straight_flush()+z.three_of_a_kind()
    #n = z.all_comb()
    #r = d/n
    #print '拿到对子及以上的概率: ',r
    #print '4个人至少有一个出对子及以上的概率', utils.repeat_rate(r, 4)
    