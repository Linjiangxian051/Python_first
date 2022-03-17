import socket

if __name__ == '__main__':
    #创建socket套接字
    tcp_client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #IPv4 tcp
    tcp_client_socket.setsockopt(socket.SOL_SOCKET,socket.SOCK_STREAM,True)
    #客服端不强制要求绑定端口
    tcp_client_socket.bind(("",8900))
    #请求连接服务端，三次握手
    tcp_client_socket.connect(("10.16.45.54",9090))

    send_content = "你好，我是客户端"
    #将字符串按utf-8的方式编码成二进制数据
    send_data = send_content.encode("utf-8")
    #发送数据
    tcp_client_socket.send(send_data)
    #接受服务端的数据
    recv_data = tcp_client_socket.recv(1024)
    print("接收服务端的数据为：",recv_data.decode("utf-8"))

    #关闭套接字
    tcp_client_socket.close()
