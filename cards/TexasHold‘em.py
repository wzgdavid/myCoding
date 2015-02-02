# encoding: utf-8
from __future__ import division #  python 3 不用
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

    def public_cards(self):
        return self.get_random_cards(5)

    def my_cards(self):
        return self.get_random_cards(2)

    def shuffle(self):
        '''洗牌'''
        self.create_cards()

    def __has_straight(self, cards):
        '''顺子'''
        index_list = []
        for card in cards:
            index_list.append(self.num_list.index(self.__num(card)))
        s = set(index_list)
        index_list = list(s)
        index_list.sort()
        cnt = 0
        for i, item in enumerate(index_list):
            if i == 0:continue
            if index_list[i-1] + 1 == item:
                cnt += 1
                if cnt >= 4:
                    return 4
            else:
                cnt = 0
        return 0

    def __has_royal_flush(self, cards):
        '''皇家同花顺'''
        pass

    def __has_straight_flush(self, cards):
        '''同花顺'''
        if not self.__has_flush(cards) or not self.__has_straight(cards):
            return 0
        suit_list = []
        # 确定同花的花色
        [suit_list.append(self.__suit(card)) for card in cards]
        c = Counter(suit_list)
        most_suit = c.most_common(1)[0][0]

        index_list = []
        for card in cards:
            if self.__suit(card) == most_suit:
                item = self.__suit(card), self.num_list.index(self.__num(card))
                index_list.append(item)
        # 排序
        sorted_list = sorted(index_list, key=itemgetter(1))
        cnt = 0
        for i, item in enumerate(sorted_list):
            if i == 0:continue
            # 后一项比前一项大1
            if sorted_list[i-1][1] + 1 == item[1]:
                cnt += 1
                if cnt >= 4:    
                    return 8
            else:
                cnt = 0
        return 0

    def __has_flush(self, cards):
        '''判断是否有同花'''
        suit_list = []
        [suit_list.append(self.__suit(card)) for card in cards]
        c = Counter(suit_list)
        if c.most_common(1)[0][1] >= 5:
            return 5
        return 0

    def __has_same_num(self, cards):
        '''判断几个相同点数的牌型，比如 对子， 三条等,逻辑相同'''
        num_list = []
        [num_list.append(self.__num(card)) for card in cards]
        c = Counter(num_list)
        most_1 = c.most_common(1)[0][1]
        most_2 = c.most_common(2)[1][1]
        # 判断顺序不能倒过来
        # 四条
        if most_1 == 4:
            return 7
        # 葫芦
        elif most_1 == 3 and most_2 == 2:
            return 6
        # 三条
        elif most_1 == 3 and most_2 == 1:
            return 3
        # 两对
        elif most_1 == 2 and most_2 == 2:
            return 2
        # 对子
        elif most_1 == 2 and most_2 == 1:
            return 1
        return 0

    def __get_points(self, cards):
        '''根据牌型取得分数'''
        points = max(
            self.__has_straight_flush(cards),  # 8 分
            self.__has_same_num(cards),        # 1 2 3 6 7
            self.__has_straight(cards),        # 5
            self.__has_flush(cards),           # 4
        )
        return points

    def judge(self, cards_one, cards_another):
        '''
        根据两手牌的牌型分数比大小，同样大小的进行同牌型的比较
        one > another 返回True
        输返回False  胜  平 都返回True
        '''
        p1 = self.__get_points(cards_one)
        p2 = self.__get_points(cards_another)
        #print p1, p2 ,' judge points'
        if p1 > p2:
            return True
        elif p1 < p2:
            return False

        if p1 == p2 == 0: # 比较高牌
            return self.__judge_gaopai(cards_one, cards_another)
        elif p1 == p2 == 1:  # 比较对子大小
            return self.__judge_pair(cards_one, cards_another)
        elif p1 == p2 == 2:  # 比较两对大小
            return self.__judge_two_pairs(cards_one, cards_another)
        elif p1 == p2 == 3:  # 比较三条大小
            return self.__judge_threeofakind(cards_one, cards_another)
        elif p1 == p2 == 4:  # 比较普通顺子大小
            return self.__judge_straight(cards_one, cards_another)
        elif p1 == p2 == 5:  # 比较同花大小
            return self.__judge_flush(cards_one, cards_another)
        elif p1 == p2 == 6:  # 比较俘虏大小
            return self.__judge_full_house(cards_one, cards_another)
        elif p1 == p2 == 7:  # 比较四条大小
            return self.__judge_fourofakind(cards_one, cards_another)
        elif p1 == p2 == 8:  # 比较同花顺大小
            return self.__judge_flush(cards_one, cards_another)
        return True

    def __judge_fourofakind(self, cards_one, cards_another):
        '''比较两幅 四条 大小'''
        num_list1 = []
        [num_list1.append(self.__num(card)) for card in cards_one]
        c1 = Counter(num_list1)
        most_num1 = self.num_list.index(c1.most_common(1)[0][0])
        num_list2 = []
        [num_list2.append(self.__num(card)) for card in cards_another]
        c2 = Counter(num_list2)
        most_num2 = self.num_list.index(c2.most_common(1)[0][0])
        if most_num1 > most_num2: #  四条不可能相等
            return True
        else: return False

    def __judge_full_house(self, cards_one, cards_another):
        '''比较两幅 俘虏 大小'''
        num_list1 = []
        [num_list1.append(self.__num(card)) for card in cards_one]
        c1 = Counter(num_list1)
        c1_most1_num = self.num_list.index(c1.most_common(1)[0][0])
        c1_most2_num = self.num_list.index(c1.most_common(2)[1][0])

        num_list2 = []
        [num_list2.append(self.__num(card)) for card in cards_another]
        c2 = Counter(num_list2)
        c2_most1_num = self.num_list.index(c2.most_common(1)[0][0])
        c2_most2_num = self.num_list.index(c2.most_common(2)[1][0])
        
        if c1_most1_num > c2_most1_num:
            return True
        elif c1_most1_num < c2_most1_num:
            return False
        # 三张一样大， 比两张
        if c1_most2_num > c2_most2_num:
            return True
        elif c1_most2_num < c2_most2_num:
            return False
        return True

    def __judge_flush(self, cards_one, cards_another):
        '''比较两幅 同花 大小'''
        # 获取同花的花色
        suit_list = []
        [suit_list.append(self.__suit(card)) for card in cards_one]
        c = Counter(suit_list)
        suit = c.most_common(1)[0][0]

        flush1 = self.__get_suit_cards(cards_one, suit)
        flush2 = self.__get_suit_cards(cards_another, suit)

        return self.__judge_gaopai(flush1, flush2)

    def __get_suit_cards(self, cards, suit):
        '''获取指定花色的牌'''
        rtn_cards = []
        [rtn_cards.append(card) for card in cards if self.__suit(card) == suit]
        return rtn_cards

    def __judge_straight(self, cards_one, cards_another):
        '''比较两幅 普通顺子 大小'''
        max_num = [0,0] # 两幅顺子中最大的那个数
        for i, cards in enumerate([cards_one, cards_another]):
            index_list = []
            for card in cards:
                index_list.append(self.num_list.index(self.__num(card)))
            sorted_list = sorted(index_list)
            index_list = list(set(sorted_list))
            for n in range(len(index_list) - 4):
                if all([
                    index_list[n] +1 == index_list[n+1],
                    index_list[n] +2 == index_list[n+2],
                    index_list[n] +3 == index_list[n+3],
                    index_list[n] +4 == index_list[n+4]]
                    ):
                    max_num[i] = index_list[n+4]
        if max_num[0] >= max_num[1]:
            return True
        else: return False

    def __judge_threeofakind(self, cards_one, cards_another):
        '''# 比较两幅三条大小'''
        num_list1 = []
        [num_list1.append(self.__num(card)) for card in cards_one]
        c1 = Counter(num_list1)
        pair_num1 = self.num_list.index(c1.most_common(1)[0][0])
        num_list2 = []
        [num_list2.append(self.__num(card)) for card in cards_another]
        c2 = Counter(num_list2)
        pair_num2 = self.num_list.index(c2.most_common(1)[0][0])
        # 对子点数比大小
        if pair_num1 > pair_num2:
            return True
        elif pair_num1 < pair_num2:
            return False
        else:
            c1 = self.__remove_num(cards_one, pair_num1)
            c2 = self.__remove_num(cards_another, pair_num1)
            return self.__judge_gaopai(c1, c2, num=2)

    def __judge_gaopai(self, cards_one, cards_another, num=5):
        '''比较两幅高牌大小
        num为比较几张牌
        '''
        lst1 = self.__sorted_cards(cards_one)
        lst2 = self.__sorted_cards(cards_another)
        for n in range(num):
            if lst1[n] >lst2[n]:
                return True
            elif lst1[n] < lst2[n]:
                return False
        return True

    def __judge_pair(self, cards_one, cards_another):
        '''比较两幅对子大小'''# 应该是去掉对子比3张大牌的大小
        num_list1 = []
        [num_list1.append(self.__num(card)) for card in cards_one]
        c1 = Counter(num_list1)
        pair_num1 = self.num_list.index(c1.most_common(1)[0][0])
        num_list2 = []
        [num_list2.append(self.__num(card)) for card in cards_another]
        c2 = Counter(num_list2)
        pair_num2 = self.num_list.index(c2.most_common(1)[0][0])
        # 对子点数比大小
        if pair_num1 > pair_num2:
            return True
        elif pair_num1 < pair_num2:
            return False
        else:
            c1 = self.__remove_num(cards_one, pair_num1)
            c2 = self.__remove_num(cards_another, pair_num1)
            return self.__judge_gaopai(c1, c2, num=3)

    def __judge_two_pairs(self, cards_one, cards_another):
        '''比较两幅 两对大小'''
        num_list1 = []
        [num_list1.append(self.__num(card)) for card in cards_one]
        c1 = Counter(num_list1)
        #pair_num1 = c1.most_common(1)[0][0]
        # 有3个对子时
        if c1.most_common(3)[2][1] == 2:
            pair_num1 = [self.num_list.index(c1.most_common(3)[0][0]),
                self.num_list.index(c1.most_common(3)[1][0]),
                self.num_list.index(c1.most_common(3)[2][0])]
        else:
            pair_num1 = [self.num_list.index(c1.most_common(2)[0][0]), self.num_list.index(c1.most_common(2)[1][0])]

        num_list2 = []
        [num_list2.append(self.__num(card)) for card in cards_another]
        c2 = Counter(num_list2)
        # 有3个对子时
        if c2.most_common(3)[2][1] == 2:
            pair_num2 = [self.num_list.index(c2.most_common(3)[0][0]),
                self.num_list.index(c2.most_common(3)[1][0]),
                self.num_list.index(c2.most_common(3)[2][0])]
        else:
            pair_num2 = [self.num_list.index(c2.most_common(2)[0][0]), self.num_list.index(c2.most_common(2)[1][0])]

        sorted1 = sorted(pair_num1, reverse=True)
        sorted2 = sorted(pair_num2, reverse=True)
        for n in [0,1]:
            if sorted1[n] >sorted2[n]:
                return True
            elif sorted1[n] < sorted2[n]:
                return False
            else:
                continue
        # 到这里是两对的大小一样， 需要比较除了两对之外最大的一张牌
        c1 = self.__remove_num(cards_one, sorted1[0])
        c1 = self.__remove_num(c1, sorted1[1])
        c2 = self.__remove_num(cards_another, sorted1[0])
        c2 = self.__remove_num(c2, sorted1[1])
        return self.__judge_gaopai(c1, c2, num=1)

    def __sorted_cards(self, cards):
        '''排序返回牌的点数'''
        card_nums = []
        for card in cards:
            card_nums.append(self.num_list.index(self.__num(card)))
        return sorted(card_nums, reverse=True)

    def __remove_num(self, cards, num):
        '''从一手牌中移除指定点数的牌
        比如  移除 所有A __remove_num(cards, 'A')
        '''
        rtn_cards = []
        for card in cards:
            if self.__num(card) != num:
                rtn_cards.append(card)
        return rtn_cards

    def test(self):
        # unit test
        #cards1 = self.get_random_cards(7)
        #cards1 = ['s_A', 'c_A', 'h_7', 's_7', 'c_Q', 'd_7', 'c_K']  # 
        #cards2 = ['s_K', 'd_8', 'h_7', 's_7', 'c_Q', 'd_7', 'c_K']  # 
        #print cards1,cards2, self.judge(cards1, cards2), '-----'

        #print self.__has_straight_flush(cards2), 'if has straight'

        '''
        my_cards手里指定牌，看与n个人玩的胜率
        '''
        my_cards = []
        op_cards = []
        #op_cards2 = []
        #op_cards3 = []
        #op_cards4 = []
        # 我的指定手牌
        #my_cards.append(self.get_card('s_A'))
        #my_cards.append(self.get_card('c_A'))

        # 我也随机
        my_cards.extend(self.get_random_cards(2))

        op_cards.extend(self.get_random_cards(2))
        #op_cards2.extend(self.get_random_cards(2))
        #op_cards3.extend(self.get_random_cards(2))
        #op_cards4.extend(self.get_random_cards(2))

        public_cards = self.get_random_cards(5)

        my_pk_cards = my_cards + public_cards
        op_pk_cards = op_cards + public_cards
        #op_pk_cards2 = op_cards2 + public_cards
        #op_pk_cards3 = op_cards3 + public_cards
        #op_pk_cards4 = op_cards4 + public_cards

        result1 = self.judge(my_pk_cards, op_pk_cards)
        return result1
        #print my_pk_cards, op_pk_cards, result1, '  **********pk cards'
        
        #result2 = self.judge(my_pk_cards, op_pk_cards2)
        #print my_pk_cards, op_pk_cards2, result2, '  **********pk cards'
        #return all([result1, result2])

        #result3 = self.judge(my_pk_cards, op_pk_cards3)
        #print my_pk_cards, op_pk_cards3, result3, '  **********pk cards'
        #return all([result1, result2, result3])
        #result4 = self.judge(my_pk_cards, op_pk_cards4)


if __name__ == '__main__':

    z = TexasHold_em()
    my_win_cnt = 0
    for n in range(10000):
        if z.test():
            my_win_cnt += 1
        z.shuffle()
    print my_win_cnt, 'my_win_cnt'
