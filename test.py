import time
import os
import serial


time_l = time.localtime()
print('time = ',time_l)
print(type(time_l))
for item in time_l:
    print(item)

date = time.strftime('%Y-%m-%d-%H-%M-%S-%A',time.localtime())
print(date)

item = 'wad'
data_type = serial.Serial.read()
print(item)

