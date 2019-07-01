import socket
import datetime     #Socker 模块
HOST='0.0.0.0'
PORT=3434
#AF_INET说明使用IPv4地址,SOCK_STREAM指明TCP
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))     #绑定IP与端口
s.listen(1)             #监听
while True:
    conn,addr=s.accept()        #接收TCP连接,并返回新的SOCKET对象
    #输出客户端的IP地址
    print('Client %s connected !'%str(addr))
    dt=datetime.datetime.now()
    #向客户端发送当前时间
    message='Current time is '+str(dt)
    conn.send(message.encode('utf8'))
    print('Sent:',message)
    #关闭连接
    conn.close()
