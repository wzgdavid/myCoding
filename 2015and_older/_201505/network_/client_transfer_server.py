# encoding: utf-8
'''
client之间通信
用udp


客户端在终端coding

for example

客户端首先发送 ready, 表示加入通信
>>> import socket, json
>>> s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
>>> data ={'uid': 1, 'ready': 'yes'}
>>> json_data = json.dumps(data)
>>> s.sendto(json_data, ('localhost', 50002))
26
>>> 

1端 发消息给 2端
>>> data ={'uid': 1, 'dstid': 2,'msg': 'hello 2'}  # uid 自己  dstid 对方
>>> json_data = json.dumps(data)
>>> s.sendto(json_data, ('localhost', 50002))
40
>>> 

此时在2端 接收
>>> s.recv(123)
'{"msg": "hello 2", "uid": 1, "dstid": 2}'
>>> 
反之亦然



'''

import json
import socket
from setting import HOST, PORT

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((HOST, PORT))

client_address = {}  # 格式  {id: address}

if __name__ == '__main__':
    while True:
        data_str, address = s.recvfrom(1024)
        if not data_str: continue;
    
        # 首次加入,发 uid 和 ready 消息 给服务器 data ={'uid': 1, 'ready': 'yes'}
        data = json.loads(data_str)
        print data
        if data.get('ready', '') == 'yes':
            client_address.update({data['uid']: address})
            print 'client_address ', client_address
            continue
        
    
        # 有目标 id 发送消息给目标
        if data['dstid'] in client_address.keys():
            s.sendto(data_str, client_address[data['dstid']])

        else:
            print 'no this dstid'
            #s.sendto(json.dumps({'msg': 'no this dstid'}), address)
        
    s.close()
