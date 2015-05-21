import socket
from time import ctime
#s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_UDP)
#s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
#while True:
#    print s.recvfrom(65535)
HOST = 'localhost'
PORT = 21567
BUFSIZE = 1024

ADDR = (HOST, PORT)


def decodeIpHeader(data):
    mapRet = {}
    mapRet["version"] = (int(ord(data[0])) & 0xF0)>>4
    mapRet["headerLen"] = (int(ord(data[0])) & 0x0F)<<2
    mapRet["serviceType"] = hex(int(ord(data[1])))
    mapRet["totalLen"] = (int(ord(data[2])<<8))+(int(ord(data[3])))
    mapRet["identification"] = (int( ord(data[4])>>8 )) + (int( ord(data[5])))
    mapRet["id"] = int(ord(data[6]) & 0xE0)>>5
    mapRet["fragOff"] = int(ord(data[6]) & 0x1F)<<8 + int(ord(data[7]))
    mapRet["ttl"] = int(ord(data[8]))
    mapRet["protocol"] = int(ord(data[9]))
    mapRet["checkSum"] = int(ord(data[10])<<8)+int(ord(data[11]))
    mapRet["srcaddr"] = "%d.%d.%d.%d" % (int(ord(data[12])),int(ord(data[13])),int(ord(data[14])), int(ord(data[15])))
    mapRet["dstaddr"] = "%d.%d.%d.%d" % (int(ord(data[16])),int(ord(data[17])),int(ord(data[18])), int(ord(data[19])))
    return mapRet


proto = socket.getprotobyname('tcp') # only tcp
print proto, socket.IPPROTO_TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, proto)
sock.bind(ADDR)
while True:
    print 'loop start'
    #data = raw_input('>')
    #if not data:
    #    break
    #sock.sendto(data,ADDR)
    data, addr = sock.recvfrom(65535)
    sock.sendto('[%s] %s'%(ctime(), data), addr)
    print 'get data'
    if len(data) == 0:
        print 'if len(data) == 0:'
        sock.close()
    else:
        print str(data)
        mapIpTmp = decodeIpHeader(data)
        for k,v in mapIpTmp.items():
                print k,"\t:\t",v
    print "loop end"