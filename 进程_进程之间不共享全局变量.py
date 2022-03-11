# g_list = list()
# print('初始化时id = ',id(g_list))
# def add_data():
#     global g_list
#     global a
#     a = 1
#     for i in range(3):
#         g_list = [i]
#     #g_list.append(i)
#     print(id(g_list),g_list[0])
#
# def modify():
#     global a
#     a = 2
#
# print('调用add函数')
# add_data()
# modify()
# print('a = ',a)
# print('global之后id: ',id(g_list))
# print(len(g_list),g_list)

import multiprocessing
import time

g_list = list()

def add_data():
    global g_list
    for i in range(3):
        print("add: ",i)
        '''
            因为列表是可变类型，可以在原有内存基础上修改数据，并且修改后内存地址不变
            所以不需要加上global关键字
            加上global 表示要修改全局变量的内存地址
        '''
        g_list.append(i)
        time.sleep(0.2)
    print("添加完成",g_list)

def read_data():
    global g_list
    print("read:",g_list)



if __name__ == '__main__':
    add_process = multiprocessing.Process(target=add_data)
    read_process = multiprocessing.Process(target=read_data)

    add_process.start()
    add_process.join()

    read_process.start()
    #进程之间不共享全局变量