# encoding: utf-8
'''
client之间通信
用udp
'''
import json
import socket
from setting import HOST, PORT

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))

clients = {}  # 格式  {id: address}
while 1:
    data_str, address = sock.recvfrom(1024)
    if not data_str: break;
    #print 'client address ',address
    print 'data', data_str
    if data_str == 'start_':
        continue

    data = json.loads(data_str)
    if address not in clients.keys():
        clients.update({data['uid']: address})
    print 'all clients connet ', clients

    # 有目标 id 发送消息给目标
    if data['dstid'] in clients.keys():
        sock.sendto(data_str, clients[data['dstid']])
    # 没有目标 id 发消息回自己
    else:
        sock.sendto(json.dumps({'msg': 'no this dstid'}), address)
    
sock.close()