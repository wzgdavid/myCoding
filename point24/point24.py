# encoding:utf-8

import itertools
import random

def add(a, b):
    return a+b, str(a)+'+'+str(b)+'='+str(a+b)

def minus(a, b):
    # 打印答案时不要有负数
    if a<b:
        return 9999, 'no'
    return a-b, str(a)+'-'+str(b)+'='+str(a-b)

def multiply(a, b):
    return a*b, str(a)+'*'+str(b)+'='+str(a*b)

def divide(a, b):
    if b == 0:
        return 9999, 'no'
    return a/b, str(a)+'/'+str(b)+'='+str(a/b)


def cal_24point(a, b, c, d):
    # a, b, c, d的排列组合
    permutation_list = list(itertools.permutations([a, b, c, d], 4))  
    # 加减乘除 排列组合
    op_list = list(itertools.permutations([add, minus, multiply, divide], 4))  
    
    # pro1 到 pro5包装函数
    # ((a, b), c), d
    def pro1(op1, op2, op3):
        m = op1(pmt[0], pmt[1])
        n = op2(m[0], pmt[2])
        result = op3(n[0], pmt[3])
        if result[0] == 24:
            #print(m[1], n[1], result[1])
            return (m[1], n[1], result[1])
    
    # (c, (a, b)), d    
    def pro2(op1, op2, op3):
        m = op1(pmt[0], pmt[1])
        n = op2(pmt[2] , m[0])
        result = op3(n[0], pmt[3])
        if result[0] == 24:
            #print(m[1], n[1], result[1])
            return (m[1], n[1], result[1])

    # d, ((a, b), c)
    def pro3(op1, op2, op3):
        m = op1(pmt[0], pmt[1])
        n = op2(m[0], pmt[2])
        result = op3(pmt[3], n[0])
        if result[0] == 24:
            #print(m[1], n[1], result[1])
            return (m[1], n[1], result[1])

    # d, (c, (a, b))
    def pro4(op1, op2, op3):
        m = op1(pmt[0], pmt[1])
        n = op2(pmt[2], m[0])
        result = op3(pmt[3], n[0])
        if result[0] == 24:
            #print(m[1], n[1], result[1])
            return (m[1], n[1], result[1]) 

    # (a b)(c d)
    def pro5(op1, op2, op3):
        m = op1(pmt[0], pmt[1])
        n = op2(pmt[2], pmt[3])
        result = op3(n[0], m[0])
        if result[0] == 24:
            #print(m[1], n[1], result[1])
            return (m[1], n[1], result[1])

    for pmt in permutation_list:
        for op in op_list:
            # 相同运算符
            if pro1(op[0], op[0], op[0]):
                return pro1(op[0], op[0], op[0])
            if pro2(op[0], op[0], op[0]):
                return pro2(op[0], op[0], op[0])
            if pro3(op[0], op[0], op[0]):
                return pro3(op[0], op[0], op[0])
            if pro4(op[0], op[0], op[0]):
                return pro4(op[0], op[0], op[0])
            if pro5(op[0], op[0], op[0]):
                return pro5(op[0], op[0], op[0])

            # ((a, b), c), d
            if pro1(op[0], op[1], op[2]):
                return pro1(op[0], op[1], op[2])
            if pro1(op[0], op[1], op[1]):
                return pro1(op[0], op[1], op[1])
            if pro1(op[0], op[0], op[1]):
                return pro1(op[0], op[0], op[1])
            if pro1(op[0], op[1], op[0]):
                return pro1(op[0], op[1], op[0])

            # (c, (a, b)), d
            if pro2(op[0], op[1], op[2]):
                return pro2(op[0], op[1], op[2])
            if pro2(op[0], op[1], op[1]):
                return pro2(op[0], op[1], op[1])
            if pro2(op[0], op[0], op[1]):
                return pro2(op[0], op[0], op[1])
            if pro2(op[0], op[1], op[0]):
                return pro2(op[0], op[1], op[0])

            # d, ((a, b), c)
            if pro3(op[0], op[1], op[2]):
                return pro3(op[0], op[1], op[2])
            if pro3(op[0], op[1], op[1]):
                return pro3(op[0], op[1], op[1])
            if pro3(op[0], op[0], op[1]):
                return pro3(op[0], op[0], op[1])
            if pro3(op[0], op[1], op[0]):
                return pro3(op[0], op[1], op[0])

            # d, (c, (a, b))
            if pro4(op[0], op[1], op[2]):
                return pro4(op[0], op[1], op[2])
            if pro4(op[0], op[1], op[1]):
                return pro4(op[0], op[1], op[1])
            if pro4(op[0], op[0], op[1]):
                return pro4(op[0], op[0], op[1])
            if pro4(op[0], op[1], op[0]):
                return pro4(op[0], op[1], op[0])

            # (a b)(c d)
            if pro5(op[0], op[1], op[2]):
                return pro5(op[0], op[1], op[2])
            if pro5(op[0], op[1], op[1]):
                return pro5(op[0], op[1], op[1])
            if pro5(op[0], op[0], op[1]):
                return pro5(op[0], op[0], op[1])
            if pro5(op[0], op[1], op[0]):
                return pro5(op[0], op[1], op[0])
    print('no result')
    return None


# ---------------------------test---------------------------------
'''
for n in range(30):
    a = random.randint(1,13)
    b = random.randint(1,13)
    c = random.randint(1,13)
    d = random.randint(1,13)
    print(a, b, c, d)
    print(cal_24point(a, b, c, d),'*'*10)
'''
