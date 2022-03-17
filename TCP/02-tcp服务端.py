import socket

if __name__ == '__main__':
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    tcp_server_socket.bind(("",9090))

    tcp_server_socket.listen(128)#listen后的套接字为被动套接字，即服务端套接字，不负责收发消息，只用来接受连接请求

    # 注意点： 每次当客户端和服务端建立连接成功都会返回一个新的套接字
    # tcp_server_socket只负责等待接收客户端的连接请求，收发消息不使用该套接字
    new_client,ip_port =  tcp_server_socket.accept()#返回一个元组（新的套接字，ip和端口）:相当于服务端10086（tcp_server_socket）给客户分配了一个客服人员（新的套接字）
    print("客户端的ip和端口号为：",ip_port)

    #当客户端的套接字调用close后，服务端的recv会解阻塞，返回数据长度为0，可以通过判断此长度来判断客户端是否已经下线,反之，客户端的recv也是如此
    recv_data = new_client.recv(1024)
    print("服务端接受的数据长度为：",len(recv_data))

    print("服务端收到的数据为：",recv_data.decode("utf-8"))
    send_data = "问题正在处理中。。。".encode("utf-8")
    new_client.send(send_data)

    # 关闭服务与客户端套接字，表示和客户端终止通信
    new_client.close()
    # 7. 关闭服务端套接字， 表示服务端以后不再等待接受客户端的连接请求，但之前已经连接成功的客服端还能正常通信
    tcp_server_socket.close()
