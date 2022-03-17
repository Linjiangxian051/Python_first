import socket

def main():
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    tcp_server_socket.bind(("", 9000))
    tcp_server_socket.listen(128)

    while True:
        new_client, ip_port = tcp_server_socket.accept()
        recv_data = new_client.recv(4096)
        if len(recv_data) == 0:
            new_client.close()
            return
        recv_content = recv_data.decode("utf-8")

        request_list = recv_content.split(" ", maxsplit=2)
        #print(request_list)
        request_path = request_list[1]
        # 若请求根目录，则返回默认的信息
        if request_path == '/':
            request_path = "/index.html"
        #当查询的资源目录或文件不存在时：
        #1.os.path.exists(path)
        #2.try-except-else-finally

        try:
            with open("static" + request_path, "rb") as rfile:
                rfile_data = rfile.read()
        except Exception as e:
            #请求的资源未找到时03-返回404页面数据.py
            print("资源文件未找到：","static" + request_path)
            with open("static/error.html","rb") as error_file:
                error_data = error_file.read()
            # 响应行
            response_line = "HTTP/1.1 404 Not Found\r\n"
            # 响应头
            response_header = "Server: PWS/1.0\r\n"
            # 空行
            response_blank = "\r\n"
            # 响应体
            response_body = error_data

            # 数据封装成http响应报文格式的数据
            response = (response_line + response_header + response_blank).encode("utf-8") + response_body

            # 发送给浏览器的响应报文数据
            new_client.send(response)
        else:
            # 响应行
            response_line = "HTTP/1.1 200 OK\r\n"
            # 响应头
            response_header = "Server: PWS/1.0\r\n"
            # 空行
            response_blank = "\r\n"
            # 响应体
            response_body = rfile_data

            # 数据封装成http响应报文格式的数据
            response = (response_line + response_header + response_blank).encode("utf-8") + response_body

            # 发送给浏览器的响应报文数据
            new_client.send(response)
        finally:
            new_client.close()


if __name__ == '__main__':
    main()



