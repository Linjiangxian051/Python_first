import threading
import time

def task():
    time.sleep(1)
    print(threading.current_thread())

if __name__ == '__main__':
    #循环创建大量线程
    for i in range(20):
        sub_thread = threading.Thread(target=task)
        sub_thread.start()

#具体执行哪个线程是由cpu调度决定的