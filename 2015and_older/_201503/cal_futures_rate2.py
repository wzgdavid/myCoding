#coding=utf-8
import time
import random
import traceback
import logging
# 创建一个logger
logger = logging.getLogger('mylogger')
logger.setLevel(logging.DEBUG)
# 创建一个handler，用于写入日志文件
fh = logging.FileHandler('test.log')
fh.setLevel(logging.DEBUG)
# 再创建一个handler，用于输出到控制台
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# 定义handler的输出格式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# 给logger添加handler
logger.addHandler(fh)
logger.addHandler(ch)
# 记录一条日志
#logger.info('foorbar')


def foo():
    p = 1000
    zhisun = 0
    zhisun_result = 0
    zhisun_day = None
    for n in range(60): # 60 days
        p += random.choice(range(-40,40))
        if not zhisun:
            if p >= 1040 or p<= 960:
                zhisun = p
        else:
            if zhisun >1000:
                if p <= 960:
                    zhisun_result = 1
                    zhisun_day = n
                    break
            if zhisun <1000:
                if p >= 1040:
                    zhisun_result = 1
                    zhisun_day = n
                    break


    return zhisun_result, zhisun_day

result = 0
days = []
for n in range(10000):
    zhisun_result, zhisun_day = foo()
    result += zhisun_result
    if zhisun_day != None:
        #print len(days)
        
        days.append(zhisun_day)
print result
days.sort()
print days[len(days)/2]

