# encoding:utf-8

import urllib, urllib2
from pprint import pprint
from collections import Counter
from bs4 import BeautifulSoup
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
all_date = []

def get_date_of_reply(tieba_name, start_page=1, end_page=1):
#def get_date_of_reply2(start=0, end=100, step=50): # old params
    global all_date
    do_range = range((start_page-1)*50, end_page*50, 50)
    for n in do_range:
        print n
        f = urllib.urlopen('http://tieba.baidu.com/f?kw=%s&ie=utf-8&pn=%s' % (tieba_name, n))

        soup = BeautifulSoup(f.read(), 'html.parser')
        #<span class="threadlist_reply_date j_reply_data" title="最后回复时间">            9-15</span>
        onepage_reply_spans = soup.find_all("span", class_="j_reply_data")
        #onepage_date_of_reply = [getattr(one_span, 'string').strip() for one_span in onepage_reply_spans]
        onepage_date_of_reply = []
        for one_span in onepage_reply_spans:
            strdate = getattr(one_span, 'string')
            if strdate:   
                onepage_date_of_reply.append(strdate.strip())
        # 不统计当天的  当天回复是用时间表示的
        if ':' in onepage_date_of_reply[0]:
            for n in onepage_date_of_reply[:]:
                if ':' in n:
                    onepage_date_of_reply.remove(n)

        all_date.extend(onepage_date_of_reply)

    return onepage_date_of_reply


#print len(get_date_of_reply(start_page=1, end_page=10))


def test():
    #all_date = get_date_of_reply(start_page, end_page)
    #print 'all_date', all_date
    tieba_name = 'python'
    gevent.joinall([
        gevent.spawn(get_date_of_reply, tieba_name, 1, 2),
        gevent.spawn(get_date_of_reply, tieba_name, 3,4),
        gevent.spawn(get_date_of_reply, tieba_name, 5,6),
        gevent.spawn(get_date_of_reply, tieba_name, 7,8),
        gevent.spawn(get_date_of_reply, tieba_name, 9,10),

    ])
    c = Counter(all_date)

    return c

#print test()

def count_date(tieba_name, startpage, endpage, num=10):
    '''
    num 一个线程处理几页
    '''
    page_range = range(startpage, endpage, num)
    threads = []
    for page in page_range:
        threads.append(gevent.spawn(get_date_of_reply, tieba_name, page, page+num-1))
    gevent.joinall(threads)
    c = Counter(all_date)
    return c

if __name__ == '__main__':
    #print test()
    print count_date('python', 200, 250, 3)
