import socket
import threading
import sys




#定义Web服务器类
class HttpWebServer(object):
    def __init__(self,port):
        tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        tcp_server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)
        tcp_server_socket.bind(("",int(port)))
        tcp_server_socket.listen(128)
        #保存创建成功的服务器套接字
        self.tcp_server_socket = tcp_server_socket

    #处理客户端的请求
    @staticmethod
    def handle_client_request(new_socket):
        recv_data = new_socket.recv(4096)
        if recv_data == "":
            print("浏览器关闭了")
            new_socket.close()
            return
        recv_data = recv_data.decode("utf-8")
        recv_content_lis = recv_data.split(" ",maxsplit=2)
        #请求资源路径
        try:
            request_path = recv_content_lis[1]
        except BaseException as e:
            request_path = '/index.html'
        print(request_path)
        if request_path == '/':
            request_path = '/index.html'
        #打开指定的页面文件
        try:
            with open("static"+request_path,"rb") as rfile:
                read_file = rfile.read()
        except BaseException as e:
            print("请求资源不存在，路径：","static"+request_path)
            with open("static/error.html","rb") as rfile:
                read_file = rfile.read()
            #响应行
            response_line = "HTTP/1.1 404 Not Found\r\n"
            #响应头
            response_header = "Server: PWS1.0\r\n"
            #空行
            response_blank = "\r\n"
            #响应体
            response_body = read_file
            #拼接
            response = (response_line+
                        response_header+
                        response_blank).encode("utf-8")+\
                       response_body
            new_socket.send(response)
        else:
            # 响应行
            response_line = "HTTP/1.1 200 OK\r\n"
            # 响应头
            response_header = "Server: PWS1.0\r\n"
            # 空行
            response_blank = "\r\n"
            # 响应体
            response_body = read_file
            # 拼接
            response = (response_line +
                        response_header +
                        response_blank).encode("utf-8") + \
                       response_body
            new_socket.send(response)
        finally:
            new_socket.close()

    #启动Web服务器进行工作：
    def start(self):
        while True:
            new_socket , ip_port = self.tcp_server_socket.accept()
            print("客户端ip和端口为：",ip_port)
            sub_socket = threading.Thread(target=self.handle_client_request,args=(new_socket,),daemon=True)
            sub_socket.start()




def main():
    argv = ['9000']

    if len(sys.argv) != 2:
        argv[0] = '9000'
    elif not sys.argv[1].isdigit():
        print("端口号应为数字")
        return
    else:
        argv = sys.argv[1:]
    print(argv)
    #创建Web服务器对象
    web_server = HttpWebServer(argv[0])
    web_server.start()





if __name__ == '__main__':
    main()



