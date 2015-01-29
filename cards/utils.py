# encoding: utf-8
from __future__ import division #  python 3 不用
import unittest 
from collections import Counter
from math import factorial as fa

def one_pair(lst):
    '''
    list中有且仅有两个元素是相同，返回True
    '''
    return only_n_same(lst, 2)


def only_n_same(lst, n):
    '''
    list中有且仅有n个元素是相同，其他各元素都不相同，返回True
    '''
    if n < 2:
        return False
    c = Counter(lst)
    most = c.most_common(2)
    if most[0][1] == n and most[1][1] == 1:
        return True
    return False


def repeat_rate(rate, repeat_times):
    '''
    几次中出一次某事件的概率
    比如掷硬币出正面，一次正面50%，掷两次出一次正面75% ， 三次就是87.5%
    '''
    if rate <= 0 or rate >=1 or repeat_times <=0:
        return -1
    if repeat_times == 1:
        return rate
    last = repeat_rate(rate, repeat_times-1)
    t_rate = (1 - last) * rate + last
    return t_rate

def C(n, m):
    # n!/[(n-m)!m!]
    if n < m:
        return -1
    return fa(n)/(fa(n-m)*fa(m))
#C(11,)
def P(n, m):
    # n!/(n-m)!
    if n < m:
        return -1
    return fa(n)/fa(n-m)

class TestCase(unittest.TestCase):
    def test_one_pair(self):
        self.assertEqual(one_pair([1,2,3,4,5]), False)
        self.assertEqual(one_pair([1,2,3,4,1]), True)
        self.assertEqual(one_pair([1,2,1,4,1]), False)
        self.assertEqual(one_pair([2,2,2]), False)
        self.assertEqual(one_pair([3,2,2]), True)
        self.assertEqual(one_pair([5,6,7,8,9,3,2,2]), True)
    
    def test_repeat_rate(self):
        self.assertEqual(repeat_rate(0.5, 1), 0.5)
        self.assertEqual(repeat_rate(0.5, 2), 0.75)
        self.assertEqual(repeat_rate(0.5, 3), 0.875)
        self.assertEqual(repeat_rate(0, 3), -1)
        self.assertEqual(repeat_rate(0.5, 0), -1)
        self.assertEqual(repeat_rate(0.5, -9), -1)

    def test_only_n_same(self):
        self.assertEqual(only_n_same([1,1,1,3,4,5,6,7,8], 3), True)
        self.assertEqual(only_n_same([1,2,3,4,5,6,1,1,7,8], 3), True)
        self.assertEqual(only_n_same([1,1,3,4,5,6,7,8], 3), False)
        self.assertEqual(only_n_same([1,3,4,5,6,7,8,5,5,5,5], 3), False)
        self.assertEqual(only_n_same('asdfasdffds', 3), False)


def __suite():
    suite = unittest.TestSuite()
    #suite.addTest(TestCase('test_one_pair'))
    #suite.addTest(TestCase('test_repeat_rate'))
    #suite.addTest(TestCase('test_only_n_same'))
    return suite

if __name__ == "__main__":  
    unittest.main(defaultTest = '__suite')
