import multiprocessing
import time

def task():
    time.sleep(1)
    print(multiprocessing.current_process())

if __name__ == '__main__':
    #循环创建大量进程
    for i in range(20):
        sub_process = multiprocessing.Process(target=task)
        sub_process.start()

#进程之间执行也是无序的，是由操作系统调度进程来决定的