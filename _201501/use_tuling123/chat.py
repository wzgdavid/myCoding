# encoding: utf-8

import os
import json
import urllib2
#from utils import pprint
import webbrowser
import time


class TulingChat(object):

    def __init__(self):
        self.key = "813020c042190505b8218c3be0bdca01"    # turing123网站
        self.apiurl = "http://www.tuling123.com/openapi/api?"
        #self.apiurl = 'http://www.tuling123.com/openapi/wechatapi?'
        self.userid = '43746'
        #os.system("clear")
        #print "---------------start----------------"

    # use for test
    def get(self):
        print "> ",
        info = raw_input()
        
        if info == ('q' or 'exit' or "quit"):
            print "- Goodbye"
            return
        self.send(info)

    # use for test
    def send(self, info):
        print 'in send'
        url = self.apiurl + 'key=' + self.key + '&info=' + info + '&userid=' +self.userid
        print '-*-*-*-**-*-*-*-*-*', url
        re = urllib2.urlopen(url).read()
        re_dict = json.loads(re)
        
        self.__process_return_json(re_dict)
        
        #pprint(re_dict)
        #self.get()

    def __process_return_json(self, re_json):
        '''处理api返回的json'''
        print re_json['text']
        if re_json['code'] == 100000:  # 返回文字
            pass
        elif re_json['code'] == 200000:  # 链接类  百度官网 京东官网
            url  = re_json.get('url', '')
            webbrowser.open_new(url)
        elif re_json['code'] == 302000:  # 新闻   例如 输入 我想看体育新闻
            print 'news', '*'*50
            self.__process_html(re_json, 'news')
        elif re_json['code'] == 304000:  # 软件下载
            print 'download software', '*'*50
        elif re_json['code'] == 305000:  # 列车
            print 'train', '*'*50
        elif re_json['code'] == 306000:  # 航班
            print 'air line', '*'*50
        elif re_json['code'] == 308000:  # 电影， 视频， 菜谱
            print 'film', '*'*50
        elif re_json['code'] == 309000:  # 酒店
            print 'hotel', '*'*50
        elif re_json['code'] == 311000:  # 价格
            print 'price', '*'*50
            self.__process_html(re_json, 'price')
        
        # 错误码处理
        elif re_json['code'] == 40002:  # 请求内容为空 
            print 'null text', '*'*50
        elif re_json['code'] == 40004:  # 当天请求次数已用完 
            print '今天累了，明天再聊吧！', '*'*50
        elif re_json['code'] == 40005:  # 暂不支持该功能 
            print '这个我无能为力'  , '*'*50
        elif re_json['code'] in [40006, 40007]:  # 服务器升级中
            print '这几天我想休息一下' , '*'*50
        elif re_json['code'] == 50000:  # 机器人设定的“学用户说话”或者“默认回答”
            print '机器人设定的“学用户说话”或者“默认回答”  什么意思， 要看看返回' , '*'*50
        pass

        return re_json['text']

    def run(self):
        #self.get()
        self.send('你好')


    def __process_html(self, re_json, what):
        '''
        把返回json整理成一个html ， 然后自动在浏览器里打开， 方便查看
        '''
        # 打开本地html文档，webbrowser.open('file:///Users/myc/Desktop/download/test.html')
        path = os.getcwd()
        html_start = '''
            <html>
                <head>
                    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
                </head>
                <body>
        '''
        html_end = '''
                </body>
            </html>
        '''
        a_list = []
        if what == 'news':
            for article in re_json['list']:
                #html of a is <a href=article['detailurl']>article['article']</a></br>
                a = '<a href=' + article['detailurl'] + '>' + article['article'] + '</a></br>'
                a_list.append(a)


        elif what == 'price':
            for item in re_json['list']:
                a = '<a href=' + item['detailurl'] + '>' + item['name'] + '</a>' + item['price'] + '</br>'
                a_list.append(a)

        html = html_start + ''.join(a_list) + html_end
        self.__save_html_and_open(path, html)


    def __save_html_and_open(self, save_path, html):
        with open(save_path + '/temp.html','wb') as down_file:
            down_file.write(html.encode('utf-8'))
        
        url = 'file://' + save_path + '/temp.html'
        webbrowser.open_new(url)

    # use for test
    def send2(self, info):
        print 'in send'
        url = self.apiurl + 'key=' + self.key + '&info=' + info + '&userid=' +self.userid

        re = urllib2.urlopen(url).read()
        re_dict = json.loads(re)
        
        self.__process_return_json(re_dict)

    def send_message(self, msg):
        url = self.apiurl + 'key=' + self.key + '&info=' + msg + '&userid=' +self.userid
        print '-*-*-*-**-*-*-*-*-*', url
        re = urllib2.urlopen(url).read()

        re_dict = json.loads(re)
        
        return self.__process_return_json(re_dict)

if __name__ == "__main__":
    chat = TulingChat()
    chat.run()
