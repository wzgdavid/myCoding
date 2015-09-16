# encoding:utf-8
import re
import urllib, urllib2
from collections import Counter
from bs4 import BeautifulSoup

'''
sample urls
http://tieba.baidu.com/f?kw=python&ie=utf-8&pn=0     #page 1
http://tieba.baidu.com/f?kw=python&ie=utf-8&pn=50    #     2
http://tieba.baidu.com/f?kw=python&ie=utf-8&pn=100   #     3
http://tieba.baidu.com/f?kw=python&ie=utf-8&pn=150   #     4
'''
def get_date_of_reply(start_page=1, end_page=1):
#def get_date_of_reply2(start=0, end=100, step=50): # old params
	all_date_of_reply = []
	#print (start_page-1)*50, end_page*50
	do_range = range((start_page-1)*50, end_page*50, 50)
	for n in do_range:
		print n
		f = urllib.urlopen('http://tieba.baidu.com/f?kw=python&ie=utf-8&pn=%s' % n)
		html_doc = f.read()

		soup = BeautifulSoup(html_doc, 'html.parser')
		#<span class="threadlist_reply_date j_reply_data" title="最后回复时间">            9-15</span>
		onepage_reply_spans = soup.find_all("span", class_="threadlist_reply_date j_reply_data")
		#print onepage_reply_spans[49].string.strip()
		onepage_date_of_reply = (getattr(one_span, 'string').strip() for one_span in onepage_reply_spans)
		#print onepage_date_of_reply
	
		all_date_of_reply.extend(onepage_date_of_reply)

		#print(len(soup.find_all("span", class_="threadlist_reply_date j_reply_data")))
	return all_date_of_reply

all_date = get_date_of_reply(start_page=1, end_page=1)
c = Counter(all_date)
print c

for n in c.keys():
	if ':' in n:
		del c[n]
print c


