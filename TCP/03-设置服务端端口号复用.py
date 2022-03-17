import socket

if __name__ == '__main__':
    tcp_servere_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    #设置端口复用：服务端程序退出后端口号立即释放
    tcp_servere_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)

    tcp_servere_socket.bind(("",9090))

    tcp_servere_socket.listen(128)

    new_client , ip_port = tcp_servere_socket.accept()
    print("当前连接的客户端的ip、端口为：",ip_port)
    recv_data = new_client.recv(1024).decode("utf-8")
    print("收到客户端的数据为：",recv_data)

    send_data  = "请求已接收，正在处理中、。。".encode("utf-8")
    new_client.send(send_data)

    new_client.close()
    tcp_servere_socket.close()