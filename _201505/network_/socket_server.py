# encoding: utf-8
import SocketServer
from SocketServer import StreamRequestHandler
from time import ctime
from prettyprint import pp
import json

host = '0.0.0.0'
port = 50006
addr = (host, port)

class Servers(StreamRequestHandler):
    def handle(self):
        print 'Connected by ', self.client_address
        #self.wfile.write('connection %s:%s at %s succeed!' % (host,port,ctime()))
        while True:
            data = self.request.recv(1024)
            #print type(data), 'type data'
            if not data:
                break
            #print 'data:', data
            #print "recv from ", self.client_address[0]
            #self.request.send(data)
            #pp(dir(self.request))
            #print help(self.request.sendto)
            self.process_data(data)

    def process_data(self, data):
        '''
        data = {
            'msg': '',
            'sendto' (ip, port),
        }
        '''
        print 'data:', data
        data = json.loads(str(data))
        if not data.get('sendto'):
            print 'no sendto'
            self.request.send(json.dumps(data))
        else:
            print 'has sendto'
            json_data = json.dumps(data)
            self.request.sendto(json_data, tuple(data['sendto']))

if __name__ == '__main__':

    print 'server is running....'
    server = SocketServer.ThreadingTCPServer(addr, Servers)
    server.serve_forever()