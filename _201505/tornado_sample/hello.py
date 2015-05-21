# encoding: utf-8
import tornado.ioloop
import tornado.web
import urllib
import os


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('hello world')
    #def post(self):
    #    #self.set_header("Content-Type", "text/plain")
    #    self.write("at MainHandler You wrote " + self.get_argument("message"))

class BaiduSite(tornado.web.RequestHandler):
    def get(self):
        a = urllib.urlopen('http://www.baidu.com')
        self.write(a.read())


class TornadoSite(tornado.web.RequestHandler):
    def get(self):
        a = urllib.urlopen('http://www.tornadoweb.cn')
        self.write(a.read())


class PostData(tornado.web.RequestHandler):
    def get(self):
        self.write('<html><body><form action="/post" method="post">' # action = '/post' 对应自己的url
                   '<input type="text" name="message">'
                   '<input type="submit" value="Submit">'
                   '</form></body></html>')

    def post(self):
        #self.set_header("Content-Type", "text/plain")
        self.write("You wrote " + self.get_argument("message"))


class RedirctBaidu(tornado.web.RequestHandler):
    def get(self):
        self.redirect('baidu')


class HelloTemplate(tornado.web.RequestHandler):
    def get(self):
        items = ["Item 1", "Item 2", "Item 3"]
        self.render(os.getcwd() + "/template.html", title="My title", items=items)


def server_start():
    application = tornado.web.Application([
        (r"/", MainHandler),     # http://127.0.0.1:8888/
        (r"/baidu", BaiduSite),  # http://127.0.0.1:8888/baidu
        (r"/tornado", TornadoSite),
        (r"/post", PostData),
        (r"/tobaidu", RedirctBaidu),
        (r"/template", HelloTemplate),
    ])
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    server_start()