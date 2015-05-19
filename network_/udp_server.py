import socket
from time import ctime

HOST = 'localhost'
PORT = 49222
BUFSIZE = 1024
ADDR = (HOST,PORT)

udpSerSock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
udpSerSock.bind(ADDR)

while True:
    print 'wating for message...'
    data, addr = udpSerSock.recvfrom(BUFSIZE)
    udpSerSock.sendto('[%s] %s'%(ctime(),data),addr)
    print '...received from and retuned to:',addr

udpSerSock.close()