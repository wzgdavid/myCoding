# encoding:utf-8
import re
import urllib, urllib2
import copy
from pprint import pprint
from collections import Counter
from bs4 import BeautifulSoup
from gevent import monkey; monkey.patch_all()
import gevent

alldata = []

def f(url):
    print('GET: %s' % url)
    resp = urllib.urlopen(url)
    data = resp.read()
    print('%d bytes received from %s.' % (len(data), url))
    global alldata
    alldata.append(data)
    return data

def asy():
    gevent.joinall([
        gevent.spawn(f, 'https://www.python.org/'),
        gevent.spawn(f, 'https://www.yahoo.com/'),
        gevent.spawn(f, 'https://github.com/'),
        gevent.spawn(f, 'http://www.shanghaiexpat.com/'),
        gevent.spawn(f, 'http://www.gevent.org/'),
        gevent.spawn(f, 'https://www.python.org/'),
        gevent.spawn(f, 'https://www.yahoo.com/'),
        gevent.spawn(f, 'https://github.com/'),
        gevent.spawn(f, 'http://www.shanghaiexpat.com/'),
        gevent.spawn(f, 'http://www.gevent.org/'),
    ])
    print 'data num is ', len(alldata)

def sy():
    alldata = []
    alldata.append(f('https://www.python.org/'))
    alldata.append(f('https://www.yahoo.com/'))
    alldata.append(f('https://github.com/'))
    alldata.append(f('http://www.shanghaiexpat.com/'))
    alldata.append(f('http://www.gevent.org/'))
    alldata.append(f('https://www.python.org/'))
    alldata.append(f('https://www.yahoo.com/'))
    alldata.append(f('https://github.com/'))
    alldata.append(f('http://www.shanghaiexpat.com/'))
    alldata.append(f('http://www.gevent.org/'))
    print 'data num is ', len(alldata)


if __name__ == '__main__':
    asy()
