# encoding: UTF-8
import random
a = 2


def windex(lst): 
    '''
    * 有权重的随机选择
    * input [[value,weight],[value,weight],[value,weight],[value,weight]]
    * output value 
    * miaoyichao
    '''
    wtotal = sum([x[1] for x in lst]) 
    n = random.uniform(0, wtotal) 
    for item, weight in lst: 
        if n < weight: 
            break 
        n = n - weight 
    return item

cnt_dict = {1:0, 2:0, 3:0, 4:0}
for n in range(10000):
    key = windex([[1,1],[2,2],[3,3],[4,4]])
    cnt_dict[key] += 1
# print cnt_dict

def anti_vowel(text):
    for n in text:
        if n in 'aeiouAEIOU':
            text = text.replace(n, '')
    return text

def anti_vowel2(text):
    return ''.join([n for n in text if n not in 'aeiouAEIOU'])

#print anti_vowel2('hellohello')

class Indexer:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __getitem__(self, key):
        if key == 'name':

            return self.name
        elif key == 'age':
            return self.age

i = Indexer('wzg', 12)
# print i['name']
# print i.__dict__
  

#编写程序，用 1，2，3……9 组成3 个三位数abc,def 和ghi，每个数字恰好
#使用一次，要求abc:def:ghi = 1:2:3。输出所有解。
#        

def listall():
    '''转换成list，然后去重，长度是9的话说明9个数字都不同'''
    for n in range(123, 334):    
        s = str(n) + str(2*n) + str(3*n)
        if '0' in s:continue
        s_set = set(s)
        if len(s_set) == 9:
            print n, 2*n, 3*n
listall()

# 进制转换
def integer_to_decimal(num, r):
    '''r 进制 整数 转成十进制'''
    reverse_num = str(num).split('.')[0][::-1]  # 12.123 => 21     12 => 21
    l = [ int(n)*(r**i) for i, n in enumerate(reverse_num) ]
    return sum(l)

def small_num_to_decimal(num, r):
    '''r 进制 小数 转成十进制'''
    if not '.' in str(num):
        return
    small_num = str(num).split('.')[1]   # 12.123 => 123
    reverse_small_num = small_num[::-1]  # 123 => 321
    for i, n in enumerate(reverse_small_num):
        if i == 0:
            result = float(n)/r
        else:
            result = (result+float(n))/r
    return result

def to_decimal(num, r):
    if '.' in str(num):
        return integer_to_decimal(num, r) + small_num_to_decimal(num, r)
    else:
        return integer_to_decimal(num, r)
print to_decimal(123.123, 8)

