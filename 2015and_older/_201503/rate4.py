#coding=utf-8

'''
价格走出某个趋势的概率
'''
import random

class Setting():
    start = 2500   # start price
    a = 50         # 止损点

def ddd():

    s = Setting.start
    a = Setting.a
    result = 0
    beishu= 3
    p = Setting.start
    for m in range(40): 
        
        p += random.randint(-100, 100)
        # 单向
        #if p <= s - a * beishu:
        #    break
        #if p >= s + a * beishu:
        #    
        #    result = 1
        #    break

        # 双向
        if p >= s + a * beishu or p<= s - a * beishu :
            result = 1
            break
        

    return result


def sequence():
    rtn = []
    p = Setting.start
    for m in range(60): 
        
        p += random.randint(-100, 100)
        rtn.append(p)

    return rtn



class Sequence():
    def __init__(self, seq_length):
        rtn = []
        p = Setting.start
        for m in range(seq_length): 
            
            p += random.randint(-50, 50)
            rtn.append(p)
        self.values = rtn
        self.cur_high = (rtn[0], 0)   #  value, index


    def get_cur_high(self, n):
        for m in range(self.cur_high[1], n):
            if self.values[m] > self.cur_high[0]:
                self.cur_high = (self.values[m], m)
        return self.cur_high[0]

    def buy_break(self):
        for value in self.values:
            if value <= Setting.start - Setting.a:
                return True
        return False

    def sell_break(self):
        for value in self.values:
            if value >= Setting.start + Setting.a:
                return True
        return False


if __name__ == '__main__':
    cnt = 0
    for n in range(9999):
        s = Sequence(60)
        if s.buy_break() and s.sell_break():
            #print min(s.values), max(s.values)
            continue
        cnt += 1
    
    print cnt
    
    #s = Sequence(60)
    #if not (s.buy_break() and s.sell_break()):
        

   