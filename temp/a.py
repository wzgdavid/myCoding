# encoding:utf-8

import urllib, urllib2
from pprint import pprint
from collections import Counter
from bs4 import BeautifulSoup

import math
import sys
'''
sample urls
http://tieba.baidu.com/f?kw=python&ie=utf-8&pn=0     #page 1
http://tieba.baidu.com/f?kw=python&ie=utf-8&pn=50    #     2
http://tieba.baidu.com/f?kw=python&ie=utf-8&pn=100   #     3
http://tieba.baidu.com/f?kw=python&ie=utf-8&pn=150   #     4

http://tieba.baidu.com/f?kw=gupiao&ie=utf-8&pn=50  #
'''



#def add():
#    print int(sys.argv[1])+ int(sys.argv[2])
#add()

def input_name():
    firstname = raw_input("input your first name")
    lastname = raw_input("input your last name")
    print firstname, lastname
#input_name()

def fs(a, c, n):
    bsum = 0
    for i in range(n):
        bn = math.floor((a+bsum*(2-c))/c)
        bsum += bn
        yield bn

fs_sequence = fs(300000, 7.2, 9)
for n in fs_sequence:
    print n
