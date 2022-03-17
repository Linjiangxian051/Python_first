import socket
import threading

def handle_client_requedt(ip_port,new_client):
    print("客户端的ip和端口号为：",ip_port[0],ip_port[1])
    while True:
        recv_data = new_client.recv(1024) #recv函数阻塞接收消息
        if len(recv_data):
            print("接受到的数据长度为:",len(recv_data))
            print("接受到的信息为：",recv_data.decode("utf-8"))
            send_data = "问题正在处理中。。。".encode("utf-8")
            new_client.send(send_data)
        else:
            print("客户端下线了")
            break
    new_client.close()

if __name__ == '__main__':
    n=0
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)
    tcp_server_socket.bind(("",9090))
    tcp_server_socket.listen(128)

    while True:
        new_client,ip_port = tcp_server_socket.accept()
        n = n+1
        if n == 2:
            break
        #使用子线程，专门用来处理客户端的消息
        sub_thread = threading.Thread(target=handle_client_requedt,args=(ip_port,new_client),daemon=True)
        sub_thread.start()

    tcp_server_socket.close()