import socket #socket模块
HOST='0.0.0.0'
PORT=3434
#AF_INET说明使用IPv4地址,SOCK_DGRAM指明UDP
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#绑定IP与端口
s.bind((HOST,PORT))
while True:
    #本次接收最大长度为1024
    data,addr=s.recvfrom(1024)
    print('Received: %s from %s'%(data,str(addr)))
s.close()