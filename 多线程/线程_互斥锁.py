import threading
import time

mutex = threading.Lock()
#全局变量
g_num1 = 0
g_num2 = 0

def task1():
    global g_num1
    mutex.acquire()
    for i in range(1000000):
        g_num1 += 1

    print("task1 finished:",g_num1)
    time.sleep(2)
    mutex.release()


def task2():
    global g_num2
    mutex.acquire()
    for i in range(1000000):
        g_num2 += 1

    print("task2 finished:", g_num2)
    mutex.release()


if __name__ == '__main__':
    task1_thread = threading.Thread(target=task1)
    task2_thread = threading.Thread(target=task2)

    task1_thread.start()
    task2_thread.start()

# 互斥锁可以保证同一时刻只有一个线程去执行代码，能够保证全局变量的数据没有问题
# 线程等待和互斥锁都是把多任务改成单任务去执行，保证了数据的准确性，但是执行性能会下降