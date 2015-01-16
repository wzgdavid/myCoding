# encoding: utf-8
from random import randint
from collections import Counter
from pprint import pprint

class Dice(object):

    @classmethod
    def sum_is(cls, n):
        cnt = 0
        rang = range(1, 7)
        for a in rang:
            for b in rang:
                for c in rang:
                    if a+b+c == n:
                        cnt += 1
        print float(cnt/216.0)

    @classmethod
    def sum_rate(cls):
        # play
        #rate = {
        #    '10': 6, '11': 6,
        #    '9': 7, '12': 7,
        #    '8': 7, '13': 7,
        #    '7': 12, '14': 12,
        #    '6': 17, '15': 17,
        #    '5': 30, '16': 30,
        #    '4': 60, '17': 60,
        #}

        # real lottery
        rate = {
            '10': 4.5, '11': 4.5,
            '9': 5, '12': 5,
            '8': 6, '13': 6,
            '7': 8, '14': 8,
            '6': 12.5, '15': 12.5,
            '5': 20, '16': 20,
            '4': 40, '17': 40,
            '3': 120,  '18': 120,
        }
        exp_dict = {} # 期望值  越高越好
        cnt = Counter()
        for n in range(4, 18):
             cnt[str(n)] = 0
        rang = range(1, 7)
        for a in rang:
            for b in rang:
                for c in rang:
                    cnt[str(a+b+c)] += 1
                    #if a+b+c == 8:
                    #    print '--------: ', a,b,c
        print 'cnt: ', cnt
        exp_dict.update(cnt)
        for k, v in exp_dict.items():
            exp_dict[k] = v * rate[k]
        pprint({'sum  exp_dict ': exp_dict})


Dice.sum_rate()

    

