# encoding: utf-8

'''
服务端应答

客户端在终端coding
for example
>>> import socket
>>> s = socket.socket()
>>> s.connect(('127.0.0.1', 50011))
>>> s.send('1')
1
>>> s.recv(111)
>>> s.close()
'''

import socket
from setting import HOST, PORT


__answer = {
    '1': 'i know you have sent 1 to me',
    '2': '2 means stupid',
    'a': 'aaaaaaaaa',
}


def msg_process(conn, data):
    if data in __answer:
        conn.send(__answer[data])
    else:
        conn.send('sorry ,i dont know what you means')


def run_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(2)
    conn, addr = s.accept()
    while True:
        data = conn.recv(1024)
        if not data: break
        msg_process(conn, data)
    conn.close()


if __name__ == '__main__':
    run_server()
