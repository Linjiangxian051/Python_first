print(1)
print('asd')
#将数据输出文件中
fp = open('C:/Users/linjiang/Desktop/a.txt','a+')
print("hello world",file=fp)
fp.close()