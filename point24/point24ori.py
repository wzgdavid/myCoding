# encoding:utf-8

import itertools
import random
import math


def add(a, b):
    return a+b, str(a)+'+'+str(b)+'='+str(a+b)

def minus(a, b):
    return a-b, str(a)+'-'+str(b)+'='+str(a-b)

def multiply(a, b):
    return a*b, str(a)+'*'+str(b)+'='+str(a*b)

def divide(a, b):
    if b == 0:
        return 99999, 'no'
    return a/b, str(a)+'/'+str(b)+'='+str(a/b)


def cal_24point(a, b, c, d):
    permutation_list = list(itertools.permutations([a, b, c, d], 4))  # a, b, c, d的排列组合
    op_list = list(itertools.permutations([add, minus, multiply, divide], 4))
    
    for pmt in permutation_list:
        for op in op_list:
            m = op[0](pmt[0], pmt[1])
            n = op[0](m[0], pmt[2])
            result = op[0](n[0], pmt[3])
            if result[0] == 24:
                print(m[1], n[1], result[1])
                return True

            # ((a, b), c), d
            m = op[0](pmt[0], pmt[1])
            n = op[1](m[0], pmt[2])
            result = op[2](n[0], pmt[3])
            if result[0] == 24:
                print(m[1], n[1], result[1])
                return True

            m = op[0](pmt[0], pmt[1])
            n = op[1](m[0], pmt[2])
            result = op[1](n[0], pmt[3])
            if result[0] == 24:
                print(m[1], n[1], result[1])
                return True            

            m = op[0](pmt[0], pmt[1])
            n = op[0](m[0], pmt[2])
            result = op[1](n[0], pmt[3])
            if result[0] == 24:
                print(m[1], n[1], result[1])
                return True 

            m = op[0](pmt[0], pmt[1])
            n = op[1](m[0], pmt[2])
            result = op[0](n[0], pmt[3])
            if result[0] == 24:
                print(m[1], n[1], result[1])
                return True 

            # (c, (a, b)), d           
            m = op[0](pmt[0], pmt[1])
            n = op[1](pmt[2], m[0])
            result = op[2](n[0], pmt[3])
            if result[0] == 24:
                print(m[1], n[1], result[1])
                return True

            m = op[0](pmt[0], pmt[1])
            n = op[1](pmt[2], m[0])
            result = op[0](n[0], pmt[3])
            if result[0] == 24:
                print(m[1], n[1], result[1])
                return True

            m = op[0](pmt[0], pmt[1])
            n = op[0](pmt[2], m[0])
            result = op[1](n[0], pmt[3])
            if result[0] == 24:
                print(m[1], n[1], result[1])
                return True

            m = op[0](pmt[0], pmt[1])
            n = op[1](pmt[2], m[0])
            result = op[1](n[0], pmt[3])
            if result[0] == 24:
                print(m[1], n[1], result[1])
                return True
            
            # d, ((a, b), c)
            m = op[0](pmt[0], pmt[1])
            n = op[1](m[0], pmt[2])
            result = op[2](pmt[3], n[0])
            if result[0] == 24:
                print(m[1], n[1], result[1])
                return True

            m = op[0](pmt[0], pmt[1])
            n = op[1](m[0], pmt[2])
            result = op[0](pmt[3], n[0])
            if result[0] == 24:
                print(m[1], n[1], result[1])
                return True

            m = op[0](pmt[0], pmt[1])
            n = op[1](m[0], pmt[2])
            result = op[1](pmt[3], n[0])
            if result[0] == 24:
                print(m[1], n[1], result[1])
                return True

            m = op[0](pmt[0], pmt[1])
            n = op[0](m[0], pmt[2])
            result = op[1](pmt[3], n[0])
            if result[0] == 24:
                print(m[1], n[1], result[1])
                return True

            # d, (c, (a, b))
            m = op[0](pmt[0], pmt[1])
            n = op[1](pmt[2], m[0])
            result = op[2](pmt[3], n[0])
            if result[0] == 24:
                print(m[1], n[1], result[1])
                return True   

            m = op[0](pmt[0], pmt[1])
            n = op[1](pmt[2], m[0])
            result = op[1](pmt[3], n[0])
            if result[0] == 24:
                print(m[1], n[1], result[1]) 
                return True

            m = op[0](pmt[0], pmt[1])
            n = op[0](pmt[2], m[0])
            result = op[1](pmt[3], n[0])
            if result[0] == 24:
                print(m[1], n[1], result[1]) 
                return True

            m = op[0](pmt[0], pmt[1])
            n = op[1](pmt[2], m[0])
            result = op[0](pmt[3], n[0])
            if result[0] == 24:
                print(m[1], n[1], result[1])            
                return True

            # (a b)(c d)
            m = op[0](pmt[0], pmt[1])
            n = op[0](pmt[2], pmt[3])
            result = op[1](n[0], m[0])
            if result[0] == 24:
                print(m[1], n[1], result[1])
                return True

            m = op[0](pmt[0], pmt[1])
            n = op[1](pmt[2], pmt[3])
            result = op[1](n[0], m[0])
            if result[0] == 24:
                print(m[1], n[1], result[1])
                return True

            m = op[0](pmt[0], pmt[1])
            n = op[1](pmt[2], pmt[3])
            result = op[0](n[0], m[0])
            if result[0] == 24:
                print(m[1], n[1], result[1])
                return True

            m = op[0](pmt[0], pmt[1])
            n = op[1](pmt[2], pmt[3])
            result = op[2](n[0], m[0])
            if result[0] == 24:
                print(m[1], n[1], result[1])
                return True
    return False


def get_random():
    return math.floor(random.random()*10+1)


for n in range(20):
    a=get_random()
    b=get_random()
    c=get_random()
    d=get_random()
    print(a, b, c, d, cal_24point(a, b, c, d), '\n')
