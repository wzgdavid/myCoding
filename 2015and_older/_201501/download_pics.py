# encoding: utf-8
import sys,urllib,re,time
from pprint import pprint

import urllib2

def get_source_urls_from(url):
    
    rtn_urls = []
    html = urllib.urlopen(url)
    data=html.read()
    #print data

    list1 = data.split('src="')

    #pprint(list1)
    for s in list1:
        want_url = s.split('"')[0]
        if want_url.startswith('http') and ( want_url.endswith('jpg') or want_url.endswith('png') ):
            rtn_urls.append(want_url)

    #pprint(rtn_urls)
    return rtn_urls


def download(from_url, save_path):
    '''
    download pics from from_url and save in save_path
    '''
    want_urls=get_source_urls_from(from_url)
    for one_url in want_urls:
        data=urllib.urlopen(one_url).read()
        with open(save_path+one_url.split('/')[-1],'wb') as down_file:
            down_file.write(data)
        print one_url
        time.sleep(0.1)
    print '结束'

download('http://www.cnblogs.com/huxi/archive/2010/07/04/1771073.html', '/Users/myc/desktop/download/test/')


