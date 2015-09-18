# encoding:utf-8
import re
import urllib, urllib2
import copy
from pprint import pprint
from collections import Counter
from bs4 import BeautifulSoup

'''
sample urls
http://tieba.baidu.com/f?kw=python&ie=utf-8&pn=0     #page 1
http://tieba.baidu.com/f?kw=python&ie=utf-8&pn=50    #     2
http://tieba.baidu.com/f?kw=python&ie=utf-8&pn=100   #     3
http://tieba.baidu.com/f?kw=python&ie=utf-8&pn=150   #     4

http://tieba.baidu.com/f?kw=gupiao&ie=utf-8&pn=50  #
'''
def get_date_of_reply(start_page=1, end_page=1):
#def get_date_of_reply2(start=0, end=100, step=50): # old params
    result = []
    do_range = range((start_page-1)*50, end_page*50, 50)
    for n in do_range:
        print n
        f = urllib.urlopen('http://tieba.baidu.com/f?kw=python&ie=utf-8&pn=%s' % n)
        #html_doc = f.read()

        soup = BeautifulSoup(f.read(), 'html.parser')
        #<span class="threadlist_reply_date j_reply_data" title="最后回复时间">            9-15</span>
        onepage_reply_spans = soup.find_all("span", class_="threadlist_reply_date j_reply_data")
        onepage_date_of_reply = [getattr(one_span, 'string').strip() for one_span in onepage_reply_spans]
        #print n, onepage_date_of_reply
        if ':' in onepage_date_of_reply[0]:
            for n in onepage_date_of_reply[:]:
                if ':' in n:
                    onepage_date_of_reply.remove(n)
        #print '2', onepage_date_of_reply
        result.extend(onepage_date_of_reply)

    return result


#print len(get_date_of_reply(start_page=1, end_page=10))


def dealwith_date(start_page=4, end_page=20):
    all_date = get_date_of_reply(start_page, end_page)
    print 'all_date', all_date
    c = Counter(all_date)

    #for n in c.keys():
    #    if ':' in n:
    #        del c[n]
    return c

print dealwith_date()
