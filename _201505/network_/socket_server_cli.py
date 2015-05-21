# encoding: utf-8
from socket_server import addr
import socket
import time
import json

s = socket.socket()
s.connect(addr)
data = {
    'sendto': ('127.0.0.1', 56415),  # 发送给终端里的那个客户端
    'name': '3'
}
s.send(json.dumps(data))
time.sleep(1)
while True:
    
    print s.recv(111)