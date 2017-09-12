import socket
from setting import HOST, PORT


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
while 1:
    data = raw_input('>')
    s.send(data)
    if not data: break
    newdata = s.recv(1024)
    print newdata
s.close()
