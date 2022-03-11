import multiprocessing
import time
import psutil
import os

def sub_task():
    print("sub_task_pid = ",os.getpid(),os.getppid())
    for i in range(10):
        print("sub程序执行中")
        time.sleep(0.2)

#当前py文件为主模块时，会执行main代码，程序入口模块
if __name__ == '__main__':
    sub_process = multiprocessing.Process(target=sub_task)
    print(sub_process)
    #把子进程设置为守护主进程
    sub_process.daemon = True
    sub_process.start()
    time.sleep(0.5)
    #立即终止子进程
    #sub_process.terminate()
    #os.kill()
    print("main over")
    for pnum in psutil.pids(): #获取所有的进程pid
        p = psutil.Process(pnum)#
        #print(p.ppid()) #获取父进程pid
        if p.name() == 'python.exe':
            print("进程名：{0}，pnum = {1}".format(p.name(),pnum))
#结论：主进程会等待子进程执行完成后程序再退出
