# encoding:utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf8")
import urllib, urllib2
from pprint import pprint
from collections import Counter, OrderedDict
from bs4 import BeautifulSoup
from jinja2 import Environment, PackageLoader


class HexunQihuo(object):
    def __init__(self):
        self.all_href = []

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

        do_range = range(670, max_idx)[::-1]
        for idx in do_range:
            print idx
            f = urllib.urlopen('http://futures.hexun.com/%s/index-%s.html' % (qtype, idx))
            soup = BeautifulSoup(f.read(), 'html.parser')
            temp01 = soup.find('div', class_='temp01')
            content = temp01.select('li > a')
            hrefs = [a['href'] +' '+ a.string for a in content if keywd in a.string]
            self.all_href.extend(hrefs)
        self.all_hrefstr = '\n'.join(self.all_href)
        return self

    def write_txt(self):
        with open('file.txt', 'w') as ff:
            ff.write(str(self.all_hrefstr))

    def write_html(self):
        env = Environment(loader=PackageLoader('hexunqihuo', 'templates'))
        data = OrderedDict()
        for href in self.all_href:
            item = href.split(' ')
            data[item[0]] = item[1]
        template = env.get_template('template.html') # templates/template.html
        html = template.render(data=data)
        htmlfile = 'files/%s.html' % self.qname
        with open(htmlfile, 'w') as ff:
            ff.write(html)


if __name__ == '__main__':

    HexunQihuo().fetch_data('industrynews', u'螺纹钢').write_html()