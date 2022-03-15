import sys
print(dir(sys))
print(sys.getsizeof(24))
print(sys.getsizeof(False))
####################
import time
print(time.time())
print(time.localtime())
print(time.localtime(time.time()))
######################################
import urllib.request

print(urllib.request.urlopen('https://music.163.com/').read())
######################################
import schedule
import time

def job():
    print('哈哈-----------')
    print('Python')

schedule.every(3).seconds.do(job)
while True:
    schedule.run_pending() #运行所有可以运行的任务
    time.sleep(1)


