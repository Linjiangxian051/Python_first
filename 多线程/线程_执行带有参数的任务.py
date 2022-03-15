import threading

def show_info(name,age):
    print("name : %s,age : %d" % (name,age))


if __name__ == '__main__':
    sub_thread = threading.Thread(target=show_info,args=('张三',20))
    sub_thread1 = threading.Thread(target=show_info,kwargs={'name':'李四','age':65})

    sub_thread.start()
    sub_thread1.start()