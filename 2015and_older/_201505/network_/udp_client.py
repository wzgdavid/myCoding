# encoding: utf-8
import socket
from setting import HOST, PORT


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while 1:
    data = raw_input('>')
    sock.sendto(data, (HOST, PORT))
    if not data: break;
    newdata = sock.recvfrom(1024)
    print newdata
sock.close()