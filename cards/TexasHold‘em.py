# encoding: utf-8
from __future__ import division #  python 3 不用
import random
from cards import Cards
from collections import Counter
from operator import itemgetter

class TexasHold_em(Cards):
    #num_list = ['2', '3','4','5','6','7','8','9','10','J','Q','K','A']

    def __num(self, card):
        return card[2:]

    def __suit(self, card):
        return card[0]

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
        #sorted_list = sorted(index_list)
        index_list.sort()
        s = set(index_list)
        index_list = list(s)
        #print index_list
        cnt = 0
        for i, item in enumerate(index_list):

            if i == 0:continue
            if index_list[i-1] + 1 == item:

                cnt += 1
                if cnt >= 4:
                    return 4
            else:
                cnt = 0
            #print i,item,'  cnt:',cnt,'in for'

        return 0

    def __has_royal_flush(self, cards):
        '''皇家同花顺'''
        pass

    def __has_test(self, cards): 
        if self.__has_flush(cards) and self.__has_straight(cards):
            return True
        else:
            return False

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
        #print sorted_list, 'sorted_list******-*-*'
        for i, item in enumerate(sorted_list):
            if i == 0:continue
            # 后一项比前一项大1
            if sorted_list[i-1][1] + 1 == item[1]:
                cnt += 1

                if cnt >= 4:    
                    return 8
            else:
                cnt = 0
            #print i,item,'  cnt:',cnt,'in for'

        return 0
    def __has_flush(self, cards):

        suit_list = []
        [suit_list.append(self.__suit(card)) for card in cards]
        c = Counter(suit_list)
        if c.most_common(1)[0][1] >= 5:
            return 5
        return 0

    def __has_same_num(self, cards):
        '''判断几个相同点数的牌型，比如 对子， 三条等'''
        num_list = []
        [num_list.append(self.__num(card)) for card in cards]
        c = Counter(num_list)
        # 四条
        if c.most_common(1)[0][1] == 4:
            return 7
        # 葫芦
        elif c.most_common(1)[0][1] == 3 and c.most_common(2)[1][1] == 2:
            return 6
        # 三条
        elif c.most_common(1)[0][1] == 3 and c.most_common(2)[1][1] == 1:
            return 3
        # 两对
        elif c.most_common(1)[0][1] == 2 and c.most_common(2)[1][1] == 2:
            return 2
        # 对子
        elif c.most_common(1)[0][1] == 2 and c.most_common(2)[1][1] == 1:
            return 1
        return 0

    def __get_points(self, cards):
        '''根据牌型取得分数'''
        points = max(
            self.__has_straight_flush(cards),  # 8
            self.__has_same_num(cards),        # 1 2 3 6 7
            self.__has_straight(cards),        # 5
            self.__has_flush(cards),           # 4
        )
        return points

    def judge(self, cards_one, cards_another):
        '''
        根据两手牌的牌型分数比大小，同样大小的继续比
        one > another 返回True
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
        return True

    def __judge_straight(self, cards_one, cards_another):
        '''比较两幅 普通顺子 大小'''

        max_num = [0,0] # 两幅顺子中最大的那个数
        for i, cards in enumerate([cards_one, cards_another]):
            index_list = []
            for card in cards:
                index_list.append(self.num_list.index(self.__num(card)))
            sorted_list = sorted(index_list)
            #s = set(sorted_list)
            #print 'sorted_list*********-*-',sorted_list
            index_list = list(set(sorted_list))
            #print 'index_list*********-*-',index_list
            for n in range(len(index_list) - 4):
                if all([
                    index_list[n] +1 == index_list[n+1],
                    index_list[n] +2 == index_list[n+2],
                    index_list[n] +3 == index_list[n+3],
                    index_list[n] +4 == index_list[n+4]]
                    ):
                    #print index_list[n+4], 'index_list[n+4]', i
                    max_num[i] = index_list[n+4]
        #print 'max_num', max_num
        if max_num[0] >= max_num[1]:
            return True
        else: return False

    def __judge_threeofakind(self, cards_one, cards_another):
        '''# 比较两幅三条大小
        直接调用对子的函数
        '''
        return self.__judge_pair(cards_one, cards_another)

    def __judge_gaopai(self, cards_one, cards_another):
        '''比较两幅高牌大小'''
        lst1 = self.__sorted_cards(cards_one)
        lst2 = self.__sorted_cards(cards_another)
        for n in range(5):
            #print lst1[n] ,lst2[n]
            if lst1[n] >lst2[n]:
                
                return True
            elif lst1[n] < lst2[n]:
                return False
        return True

    def __judge_pair(self, cards_one, cards_another):
        '''比较两幅对子大小'''
        num_list1 = []
        [num_list1.append(self.__num(card)) for card in cards_one]
        c1 = Counter(num_list1)
        pair_num1 = c1.most_common(1)[0][0]
        num_list2 = []
        [num_list2.append(self.__num(card)) for card in cards_another]
        c2 = Counter(num_list2)
        pair_num2 = c2.most_common(1)[0][0]
        # 对子点数比大小
        if pair_num1 > pair_num2:
            return True
        elif pair_num1 < pair_num2:
            return False
        else:
            return self.__judge_gaopai(cards_one, cards_another)

    def __judge_two_pairs(self, cards_one, cards_another):
        '''比较两幅 两对大小'''
        num_list1 = []
        [num_list1.append(self.__num(card)) for card in cards_one]
        c1 = Counter(num_list1)
        #pair_num1 = c1.most_common(1)[0][0]
        # 有3个对子时
        if c1.most_common(3)[2][1] == 2:
            pira_num1 = [c1.most_common(3)[0][0], c1.most_common(3)[1][0], c1.most_common(3)[2][0]]
        else:
            pira_num1 = [c1.most_common(2)[0][0], c1.most_common(2)[1][0]]


        num_list2 = []
        [num_list2.append(self.__num(card)) for card in cards_another]
        c2 = Counter(num_list2)
        # 有3个对子时
        if c2.most_common(3)[2][1] == 2:
            pira_num2 = [c2.most_common(3)[0][0], c2.most_common(3)[1][0], c2.most_common(3)[2][0]]
        else:
            pira_num2 = [c2.most_common(2)[0][0], c2.most_common(2)[1][0]]

        sotred1 = sorted(pira_num1, reverse=True)
        sotred2 = sorted(pira_num2, reverse=True)
        for n in [0,1]:
            if sotred1[n] >sotred2[n]:
                
                return True
            elif sotred1[n] < sotred2[n]:
                return False
        return self.__judge_gaopai(cards_one, cards_another)

    #def __has_card(self, cards)
    def __sorted_cards(self, cards):
        '''排序返回牌的点数'''
        card_nums = []
        for card in cards:
            card_nums.append(self.num_list.index(self.__num(card)))
        return sorted(card_nums, reverse=True)

    def test(self):
        #cards1 = self.get_random_cards(7)
        #cards1 = ['c_A', 'c_4', 'c_5', 'c_6', 'c_7', 'd_8', 'h_10']
        #cards2 = ['c_4', 'c_5', 'c_6', 'c_7', 'c_K', 'd_9', 'h_8']
        '''
        my_cards手里指定牌，看与n个人玩的胜率
        '''
        my_cards = []
        op_cards = []
        op_cards2 = []
        my_cards.append(self.get_card('s_K'))
        my_cards.append(self.get_card('c_K'))
        op_cards.extend(self.get_random_cards(2))
        op_cards2.extend(self.get_random_cards(2))
        #op_cards.append(self.get_card('c_2'))
        #op_cards.append(self.get_card('s_3'))
        public_cards = self.get_random_cards(5)

        my_pk_cards = my_cards + public_cards
        op_pk_cards = op_cards + public_cards
        op_pk_cards2 = op_cards2 + public_cards
        #print my_pk_cards, op_pk_cards, '  **********pk cards'
        result1 = self.judge(my_pk_cards, op_pk_cards)
        result2 = self.judge(my_pk_cards, op_pk_cards2)
        #print result
        return result1 and result2
        #print cards1,cards2, self.__judge_straight(cards1, cards2), '-----'


if __name__ == '__main__':

    z = TexasHold_em()
    #print z.cards
    my_win_cnt = 0
    for n in range(10000):

        if z.test():
            my_win_cnt += 1
        #z.test()
        z.shuffle()
    print my_win_cnt
