import threading
import time

#定义全局变量
g_num = 0#不可变类型，不能在原有内存地址上修改数据，所以每次都要给它开辟一个新的内存空间


def task1():
    global g_num # 表示要声明修改全局变量的内存地址
    for i in range(1000000):
        g_num += 1;
    print("task1 finished :",g_num)

def task2():
    global g_num
    for i in range(1000000):
        g_num += 1

    print("task2 finished :", g_num)


if __name__ == '__main__':
    task1_thread = threading.Thread(target=task1)
    task2_thread = threading.Thread(target=task2)
#
    # task1_thread.start()
    # task2_thread.start()
    # time.sleep(3)
    # print("main over :",g_num)
#解决方案
    task1_thread.start()
    # 线程等待，让第一个线程先执行，然后在让第二个线程再执行，保证数据不会有问题
    task1_thread.join()

    task2_thread.start()
    #print("main over :", g_num)