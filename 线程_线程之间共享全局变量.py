import threading
import time

#定义全局变量
g_list = []

def add_data():
    for i in range(3):
        g_list.append(i)
        print("add: ",i)
        time.sleep(0.2)
    print("数据加载完毕。。。",g_list)

def read_data():
    print("read: ",g_list)

if __name__ == '__main__':
    add_thread = threading.Thread(target=add_data)
    read_thread = threading.Thread(target=read_data)

    add_thread.start()
    add_thread.join()
    read_thread.start()