# encoding:utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf8")
import urllib, urllib2
from pprint import pprint
from collections import Counter
from bs4 import BeautifulSoup

all_href = []
def get_max_index(soup):
    listdh = soup.find('div', class_='listdh')
    s1 = str(listdh).split('maxPage = ')[1]
    s2 = s1.split(';')[0]
    return int(s2)
'''
with open(filename) as f:
   input = f.read()
output = do_something(input)
with open(filename, 'w') as f:
   f.write(output)
'''
def fetch_data(qtype, qname):
    '''
	                           qtype 
	# http://futures.hexun.com/industrynews/index.html') # 金属
    # http://futures.hexun.com/agriculturenews/index.html') # 农副资讯 
    # http://futures.hexun.com/nyzx/index.html  # 能源资讯
	'''
    global all_href
    #f = urllib.urlopen('http://futures.hexun.com/industrynews/index.html') # 金属
    #f = urllib.urlopen('http://futures.hexun.com/agriculturenews/index.html') # 农副资讯 
    # http://futures.hexun.com/nyzx/index.html  # 能源资讯
    f = urllib.urlopen('http://futures.hexun.com/%s/index.html' % qtype) #
    soup = BeautifulSoup(f.read(), 'html.parser')
    keywd = qname.decode('utf-8')
    temp01 = soup.find('div', class_='temp01')
    content = temp01.select('li > a')
    hrefs = [a['href'] +' '+ a.string for a in content if keywd in a.string]
    all_href.extend(hrefs)
    #if hrefs:
    #	print 'index'
    #    pprint(hrefs)
    max_idx = get_max_index(soup)
    do_range = range(1685, max_idx)[::-1]
    for idx in do_range:
        print idx
        f = urllib.urlopen('http://futures.hexun.com/%s/index-%s.html' % (qtype, idx))
        soup = BeautifulSoup(f.read(), 'html.parser')
        temp01 = soup.find('div', class_='temp01')
        content = temp01.select('li > a')
        #print(content.prettify())
        #hrefs = [a['href'] for a in content if keywd in a.string]
        hrefs = [a['href'] +' '+ a.string for a in content if keywd in a.string]
        #links = {a['href']: a.string for a in content if keywd in a.string}
        #pprint(links)
        #links = []
        #for a in content:
        #    if keywd in a.string:
        #        d = {'url': a['href'], 'title': a.string}
        #        links.append(d)
        #if hrefs:
            #pprint(hrefs)
        all_href.extend(hrefs)
    #pprint(all_href)
    all_hrefstr = '\n'.join(all_href)

    
    #with open('file.txt', 'w') as ff:
    #    ff.write(str(all_hrefstr))
    return all_hrefstr


def write_txt(data):
    with open('file.txt', 'w') as ff:
        ff.write(str(data))

data = fetch_data('agriculturenews', u'豆粕')
write_txt(data)
#class Hexun():
#	def __init__(self):
#		self.f = 
#		self.soup
