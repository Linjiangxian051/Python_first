import multiprocessing
import time

def dance():
    for i in range(3):
        print('正在跳舞。。。')
        time.sleep(1)

def sing():
    for i in range(3):
        print('正在唱歌。。')
        time.sleep(2)

#创建子进程
dance_process  = multiprocessing.Process(target=dance)
sing_process   = multiprocessing.Process(target=sing)

if __name__ == '__main__':
    dance_process.start()
    sing_process.start()
    time.sleep(1)
    sing_process.terminate()