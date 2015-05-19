# encoding: utf-8
import SocketServer
from SocketServer import StreamRequestHandler
from time import ctime
from prettyprint import pp

host = '0.0.0.0'
port = 50002
addr = (host, port)

class Servers(StreamRequestHandler):
    def handle(self):
        print 'Connected by ',self.client_address
        #self.wfile.write('connection %s:%s at %s succeed!' % (host,port,ctime()))
        while True:
            data = self.request.recv(1024)
            if not data:
                break
            print 'data:', data
            print "recv from ", self.client_address[0]
            self.request.send(data)
            #pp(dir(self.request))
            print help(self.request.sendto)

    def process_data(self, data):
        '''
        data = {
            'msg': '',
            'sendto' (ip, port),
        }
        '''
        if not data.get('sendto'):
            return

print 'server is running....'
server = SocketServer.ThreadingTCPServer(addr, Servers)
server.serve_forever()