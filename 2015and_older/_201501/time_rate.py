#/usr/bin/python
#encoding=utf8
import math
import time, os, sched


def time_rate(rate, n=1):
    '''
    返回rate的概率n次不出现的概率
    '''
    return math.pow(1-rate, n)
    
def get_times(rate, n_rate):
    '''
    返回rate的概率n次不出现的概率小于n_rate的这个n
    '''
    for n in range(1, 999):
        if time_rate(rate, n) <= n_rate:
            return n
    return 1000

if __name__ == '__main__':
    print time_rate(0.22, 18)
    print get_times(6.0/216, 0.01)