# encoding: utf-8
# Echo server program

'''
客户端在终端coding

for example
Python 2.7.5 (default, Aug 25 2013, 00:04:04) 
[GCC 4.2.1 Compatible Apple LLVM 5.0 (clang-500.0.68)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import socket
>>> s = socket.socket()
>>> s.connect(('127.0.0.1', 50011))
>>> s.send('asd')
3
>>> print s.recv(111)
asd ---- data from server
>>> 
'''
import socket
import threading

def echo(conn, addr):
    print 'Connected by', addr
    while True:
        data = conn.recv(1024)
    
        if data: 
            conn.sendall(data + ' ---- data from server ')
        else:
            conn.sendall('no data were sent from client ')


HOST = ''
PORT = 50002
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)


while True:
    conn, addr = s.accept()
    thread = threading.Thread(target=echo, args=(conn, addr))
    thread.start()
conn.close()
