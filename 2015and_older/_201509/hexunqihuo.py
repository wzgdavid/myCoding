# encoding:utf-8
'''
集中 和讯期货 一个品种的咨询
'''
import sys
reload(sys)
sys.setdefaultencoding("utf8")
import urllib, urllib2
import json
from pprint import pprint
from collections import Counter, OrderedDict
from bs4 import BeautifulSoup
from jinja2 import Environment, PackageLoader
import redis
import gevent
from gevent import monkey; monkey.patch_all()


class RedisAccess(object):
    def __init__(self):
        self.r = redis.Redis(host='localhost', port=6379, db=0)

    def get(self, key):
        return self.r.get(key)

    def set(self, key, value):
        self.r.set(key, value)

    def savedict(self, key, dict_data):
        json_data = json.dumps(dict_data)
        self.r.set(key, json_data)

    def getdict(self, key):
        json_data = self.r.get(key)
        data = json.loads(json_data)
        return data

myredis = RedisAccess()


class HexunQihuo(object):
    def __init__(self):
        self.all_href = []
        #self.redis = RedisAccess()

    def __get_max_index(self, soup):
        listdh = soup.find('div', class_='listdh')
        s1 = str(listdh).split('maxPage = ')[1]
        s2 = s1.split(';')[0]
        return int(s2)

    def fetch_data(self, qtype, qname):
        '''
          qtype is in [industrynews, agriculturenews, nyzx] 
        # http://futures.hexun.com/industrynews/index.html') # 金属
        # http://futures.hexun.com/agriculturenews/index.html') # 农副资讯 
        # http://futures.hexun.com/nyzx/index.html  # 能源资讯
        '''
        self.qtype = qtype
        self.qname = qname
        f = urllib.urlopen('http://futures.hexun.com/%s/index.html' % qtype) #
        soup = BeautifulSoup(f.read(), 'html.parser')
        keywd = qname.decode('utf-8')
        temp01 = soup.find('div', class_='temp01')
        content = temp01.select('li > a')
        hrefs = [a['href'] +' '+ a.string for a in content if keywd in a.string]
        self.all_href.extend(hrefs)
        max_idx = self.__get_max_index(soup)

        do_range = range(201, max_idx)[::-1]
        for idx in do_range:
            print idx
            f = urllib.urlopen('http://futures.hexun.com/%s/index-%s.html' % (qtype, idx))
            soup = BeautifulSoup(f.read(), 'html.parser')
            temp01 = soup.find('div', class_='temp01')
            content = temp01.select('li > a')
            hrefs = [a['href'] +' '+ a.string for a in content if keywd in a.string]
            self.all_href.extend(hrefs)
        
        return self

    def write_txt(self):
        self.all_hrefstr = '\n'.join(self.all_href)
        with open('file.txt', 'w') as ff:
            ff.write(str(self.all_hrefstr))

    def write_html(self):
        env = Environment(loader=PackageLoader('hexunqihuo', 'templates'))
        data = OrderedDict()
        for href in self.all_href:
            item = href.split(' ')
            data[item[0]] = item[1]
        #self.redis.savedict(self.qname, data)
        template = env.get_template('template.html') # templates/template.html
        html = template.render(data=data)
        htmlfile = 'files/%s.html' % self.qname
        with open(htmlfile, 'w') as ff:
            ff.write(html)

    def update_html(self):
        pass

def write_html(qtype, qname):
    HexunQihuo().fetch_data(qtype, qname).write_html()

def multi_write_html():
    gevent.joinall([
        gevent.spawn(write_html, 'agriculturenews', u'玉米'),
        gevent.spawn(write_html, 'agriculturenews', u'豆粕'),
        gevent.spawn(write_html, 'agriculturenews', u'鸡蛋'),
        gevent.spawn(write_html, 'nyzx', 'TA'),
        gevent.spawn(write_html, 'industrynews', u'铁矿'),

    ])


if __name__ == '__main__':
    #HexunQihuo().fetch_data('agriculturenews', u'玉米').write_html()
    #write_html('nyzx', 'TA')
    #print type(myredis.getdict('玉米'))

    multi_write_html()
