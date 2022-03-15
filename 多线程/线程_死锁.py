#死锁：一直等待对方释放锁的情景叫做死锁
#需求：多线程同时根据下标在列表中取值，要保证同一时刻只有一个线程去取值
import threading
import time

mutex = threading.Lock()

def get_value(index):
    #上锁
    mutex.acquire()
    my_list = [1,4,6]
    #判断下标是否越界
    if index >= len(my_list):
        print("下标越界",index)
        # 取值不成功，也需要释放互斥锁，不要影响后面的线程去取值
        # 锁需要在合适的地方进行释放，防止死锁
        time.sleep(1)
        mutex.release()
        return
    print(my_list[index])

    #释放锁
    mutex.release()



if __name__ == '__main__':
    #创建大量的线程，同时执行根据下标取值的任务
    for i in range(10):
        sub_thread = threading.Thread(target=get_value,args=(i,))
        sub_thread.start()


