# encoding: utf-8

import socket
from setting import HOST, PORT

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))
while 1:
    data, address = sock.recvfrom(1024)
    if not data: break;
    sock.sendto(data, address)
sock.close()