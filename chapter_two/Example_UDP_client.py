import socket
HOST='127.0.0.1'
POST=3434
#AF_INET说明使用IPv4地址,SOCK_DGRAM指明UDP
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
data='Hello UDP!'
s.sendto(data.encode('utf-8'),((HOST,POST)))
print('Sent:%s to %s:%d'%(data,HOST,POST))
s.close()