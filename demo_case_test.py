#列出指定目录下的所有py文件
import os
path = os.getcwd() #获取当前的工作目录
print(path)
lst = os.listdir(path)
for filename in lst:
    if filename.endswith('.py'):
        print(filename)
#path_ch = os.path.join(path,'package')
#print('当前工作目录为：',path_ch)
lst_files = os.walk('../') #获取指定目录下的迭代体对象，元组类型,[(路径，文件夹，文件名)]
for dirpath,dirname,filename in lst_files:
    # print(dirpath)
    # print(dirname)
    # print(filename)
    # print('-----------------------------------------------------------------------------------------')
    for dir in dirname:
        print(os.path.join(dirpath,dir))
    for file in filename:
        print(os.path.join(dirpath,file)+)
    print('-----------------------------------------------------------------------------------------')
lst_t = [('Jack',20,'lol'),('Jam',32,'Music'),('Mare',43,'ball')]
for i,j,k in lst_t:
    print(i)
    print(j)
    print(k)
    print('-----------------------------------------------------------------------------------------')
print('\\')