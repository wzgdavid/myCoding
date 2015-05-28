# encoding: utf-8
'''
client之间通信
用udp
'''
import json
import socket
from setting import HOST, PORT
import threading

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def recv_data(sock):
    recvdata = sock.recvfrom(1024)
    data = json.loads(recvdata[0])
    print type(data), data

while 1:
    data = {}


    #data['dst_address'] =   # 目的地址
    uid = raw_input('please input your uid >')
    data['uid'] = uid
    data['dstid'] = raw_input('please input dstid >')
    msg = raw_input('input you msg>')
    data['msg'] = msg

    json_data = json.dumps(data)
    sock.sendto(json_data, (HOST, PORT))
    #print sock.getsockname()
    if not msg: break;
    thread = threading.Thread(target=recv_data, args=(sock,))
    thread.start()
sock.close()