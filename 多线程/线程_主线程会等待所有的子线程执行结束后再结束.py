import threading
import time

def task():
    while True:
        print("任务执行中。。。")
        time.sleep(0.2)


if __name__ == '__main__':
    sub_thread = threading.Thread(target=task,daemon=True)
    #sub_thread.daemon  = True
    #sub_thread.setDaemon(True) #被淘汰
    sub_thread.start()
    time.sleep(2)
    print("main over")
