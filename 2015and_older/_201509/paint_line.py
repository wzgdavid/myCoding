
import random
import matplotlib.pyplot as plt


#matplotlib 画一个随机数值的曲线
def random_line():
    # 产生x y
    x = range(150)
    a = 2000
    y = []
    for n in x:
        a += random.randint(-5, 5)
        y.append(a)
    line, = plt.plot(x, y)
    plt.show()

random_line()
# 止损点设为10点，不碰止损的概率
def gailv():
    total_cnt = 9999
    x = range(100)
    start = 2000 # 起始点位
    a = start
    r = range(total_cnt)
    zs = 10  # 止损点
    zsd = start - zs
    #print(zsd)
    ok_cnt = total_cnt  # 不碰止损的计数
    for i in r:
        a = start
        for n in x:
            
            a += random.randint(-4, 4)
            if a <= zsd:
                ok_cnt -= 1
                break

    return ok_cnt, total_cnt


def zhiszhiy():
    '''
    开仓之后固定止损止盈, 以买多为例
    '''
    exam_times = 9999   # 实验次数
    start = 2000
    win_cnt = 0
    looss_cnt = 0
    #for i in exam_times:
    minutes = range(150)
    zsfd = 10  #止损止盈幅度
    zyfd = 15
    zsdian = start - zsfd   # 止损止盈点位
    zydian = start + zyfd   # 止损止盈点位
    while exam_times > 0:
        price = start
        for n in minutes:
            
            price += random.randint(-4, 4)
            if price <= zsdian:
                looss_cnt += 1
                
                break
            if price >= zydian:
                win_cnt += 1
                
                break
        exam_times -= 1
    return win_cnt * (zyfd/zsfd), looss_cnt


def yidongzhishun():
    '''
    移动止损, 以买多为例
    '''
    exam_times = 9999   # 实验次数
    start = 2000
    win_cnt = 0
    looss_cnt = 0
    #for i in exam_times:
    minutes = range(150)
    zsfd = 10  #开仓止损的幅度
    ydzsfd = 10  # 移动止损的幅度
    zsdian = start - zsfd   # 开仓止损点位
    ydzsdian = zsdian       # 移动止损的点位
    while exam_times > 0:
        price = start
        for n in minutes:
            
            price += random.randint(-4, 4)
            if price <= zsdian:
                looss_cnt += 1
                break
            if price - ydzsdian > ydzsfd:
                ydzsdian = price - ydzsfd
                win_cnt += 1
                
                break
        exam_times -= 1
    return win_cnt * (zyfd/zsfd), looss_cnt

    
class Account(object):

    def __init__(total_money=100000):
        self.total_money = total_money

    def buy_open(money):
        self.total_money -= money

    def sell_open(money):
        self.total_money -= money

    def offset(money):
        self.total_money += money