import multiprocessing

#显示信息
def show_info(name,age):
    print('name= ',name,'age = ',age)

if __name__ == '__main__':
    show_info_process = multiprocessing.Process(name="show_process",target=show_info,kwargs={"age":'zhangsan'},args=(99,))#优先依次传送元组里的位置参数，要保证kwargs中的字典key值不要和元组里发生冲突
    show_info_process.start()