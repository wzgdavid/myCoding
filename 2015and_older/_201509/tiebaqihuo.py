# encoding:utf-8
'''
统计期货吧的帖子 列出指定关键词的标题和url 写入html文件
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

'''
sample urls
http://tieba.baidu.com/f?kw=python&ie=utf-8&pn=0     #page 1
http://tieba.baidu.com/f?kw=python&ie=utf-8&pn=50    #     2
http://tieba.baidu.com/f?kw=python&ie=utf-8&pn=100   #     3
http://tieba.baidu.com/f?kw=python&ie=utf-8&pn=150   #     4

http://tieba.baidu.com/f?kw=gupiao&ie=utf-8&pn=50  #
'''

class TiebaQihuo(object):
    def __init__(self, qnames):
    	self.qnames = qnames
        self.all_links = {qname:OrderedDict()  for qname in qnames}
        

    def fetch_data(self, start_page=1, end_page=10):
        do_range = range((start_page-1)*50, end_page*50, 50)

        for n in do_range:
            print n
            f = urllib.urlopen('http://tieba.baidu.com/f?kw=期货&ie=utf-8&pn=%s' % n)
            soup = BeautifulSoup(f.read(), 'html.parser')
            title_links = soup.find_all("a", class_="j_th_tit")
            #print title_link
            #<a href="/p/4065231280" title="xxxxxx" target="_blank" class="j_th_tit">xxxxxx</a>
            for one in title_links:
                title = one.string
                for qname in self.qnames:
                    if qname in title:
                        # http://tieba.baidu.com/p/4069585801
                        url = 'http://tieba.baidu.com' + one['href']
                        #self.all_links[qname].update({url: title})
                        self.all_links[qname][url] = title
        #pprint(self.all_links)

    def write_html(self):
        env = Environment(loader=PackageLoader('tiebaqihuo', 'templates'))
        

        for qname in self.qnames:

            template = env.get_template('template.html') # templates/template.html
            html = template.render(data=self.all_links[qname])
            htmlfile = 'files/tieba%s.html' % qname
            with open(htmlfile, 'w') as ff:
                ff.write(html)

if __name__ == '__main__':
    tq = TiebaQihuo([u'铁矿', u'螺纹', u'玉米', u'豆粕', u'豆油', 'TA', u'白银', u'郑醇'])
    tq.fetch_data(end_page=100)
    tq.write_html()