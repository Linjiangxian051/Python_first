import multiprocessing
import os
import time

def dance():
    #获取当前进程编号
    print('---------获取dance进程编号-------------')
    dance_process_pid = os.getpid()
    #获取当前进程对象，查看当前代码是由哪个进程执行的：multiprocessing_cureent_process
    print('dance_process_id: ',dance_process_pid,multiprocessing.current_process())
    #获取当前父进程编号
    dance_process_parent_pid = os.getppid()
    print("dance_process_parent_pid: ",dance_process_parent_pid)
    for i in range(3):
        print('正在跳舞。。。')
        time.sleep(0.2)
        #os.kill(dance_process_pid,9)


def sing():
    #获取当前进程编号
    print('---------获取sing进程编号-------------')
    sing_process_pid = os.getpid()
    print("sing_process_id: ",sing_process_pid,multiprocessing.current_process())
    #获取父进程编号
    sing_process_parent_pid = os.getppid()
    print("sing_process_parent_pid",sing_process_parent_pid)

    for i in range(3):
        print('正在唱歌。。')
        time.sleep(0.2)

'''
 提示： 对应linux和mac主进程执行的代码不会进程拷贝，但是对应window系统来说主进程执行的代码，子进程也会进行拷贝执行
 对应window来说创建子进程的代码如果进程拷贝执行相当于递归无限制进行创建子进程，会报错

 如何解决windows递归创建子进程，通过判断是否是主模块来解决

 理解说明： 直接执行的模块就是主模块，那么直接执行的模块里面，就应该添加判断是否是主模块的代码if __name__ == '__main__':

 1. 防止别人导入文件的时候执行main里面的代码
 2. 防止windows系统递归创建子进程
 if __name__ == '__main__':
'''

# # 获取主进程编号
# print('---------获取主进程编号-------------')
# main_process_pid = os.getpid()
# print("main_process_pid:", main_process_pid, '\n', multiprocessing.current_process())
#
# # 创建子进程
# print('---------创建子进程-------------')
# dance_process = multiprocessing.Process(target=dance, name="dance_process")
# print("dance_process:", dance_process)
# sing_process = multiprocessing.Process(target=sing, name="sing_process")
# print("sing_process:", sing_process)


if __name__ == '__main__':
    # 获取主进程编号
    print('---------获取主进程编号-------------')
    main_process_pid = os.getpid()
    print("main_process_pid:", main_process_pid, '\n', multiprocessing.current_process())

    # 创建子进程
    print('---------创建子进程-------------')
    dance_process = multiprocessing.Process(target=dance, name="dance_process")
    print("dance_process:", dance_process)
    sing_process = multiprocessing.Process(target=sing, name="sing_process")
    print("sing_process:", sing_process)
    print('---------子进程启动-------------')
    dance_process.start()
    time.sleep(1)
    sing_process.start()
    # time.sleep(1)
    # sing_process.terminate()