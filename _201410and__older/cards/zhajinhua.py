# encoding: utf-8
from __future__ import division #  python 3 不用
from itertools import combinations
from math import factorial as fa
from utils import repeat_rate
from cards import Cards

class ZJH(Cards):

    def all_comb(self):
        '''
        所有组合数
        '''
        # n!/[(n-m)!m!] n=52 m=7
        return fa(52)/(fa(49)*fa(3))

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
        all_patterns = combinations(self.cards, 3)
        for a_hand in all_patterns:
            if cond_dict[condition](a_hand):
                cnt += 1
        return cnt

    def pair(self):
        '''对子数量'''
        return self.func('pair')

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
        n1 = self.__num(t[0])
        n2 = self.__num(t[1])
        n3 = self.__num(t[2])
        a = n1 == n2 and n1 != n3
        b = n2 == n3 and n2 != n1
        c = n1 == n3 and n1 != n2
        return any([a, b, c])

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



z = ZJH()
'''
print z.all_comb()
print z.three_of_a_kind()
print z.straight_flush()
print z.normal_flush()
print z.normal_straight()
print z.pair()
print z.normal()
print z.single_A()
'''
d = z.pair()+z.normal_straight()+z.normal_flush()+z.straight_flush()+z.three_of_a_kind()
n = z.all_comb()
r = d/n
print '拿到对子及以上的概率: ',r
print '4个人至少有一个出对子及以上的概率', repeat_rate(r, 4)  # 近70%
