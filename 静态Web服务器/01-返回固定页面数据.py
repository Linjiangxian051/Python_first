import socket

if __name__ == '__main__':
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)
    tcp_server_socket.bind(("",9000))
    tcp_server_socket.listen(128)

    while True:
        new_client,ip_port = tcp_server_socket.accept()
        recv_data = new_client.recv(4096).decode("utf-8")
        print(recv_data)

        with open("static/index.html","r") as rfile:
            rfile_data = rfile.read()

        #响应行
        response_line = "HTTP/1.1 200 OK\r\n"
        #响应头
        response_header = "Server: PWS/1.0\r\n"
        #空行
        response_blank = "\r\n"
        #响应体
        response_body = rfile_data

        #数据封装成http响应报文格式的数据
        response = response_line + response_header + response_blank +response_body
        #把字符串编码成二进制格式
        response_data = response.encode("utf-8")

        #发送给浏览器的响应报文数据
        new_client.send(response_data)
        new_client.close()



