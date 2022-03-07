###########################################
#异常处理机制
# try:
#     n1 = int(input('请输入一个整数'))
#     n2 = int(input('请输入另一个整数'))
#     result = n1 / n2
# except BaseException as e:
#     print('出错了',e)
# else:
#     print('结果为：',result)
# finally:
#     print('无论是否产生异常，总会被执行的代码')
# print('程序结束')

import traceback
try:
    print('----------------------------------')
    print(1/1)
except:
    traceback.print_exc()