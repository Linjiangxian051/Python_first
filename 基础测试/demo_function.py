############################################
#函数的创建
def calc(a,b):
    c = a + b
    return c

result = calc(10,20)
print(result)

res = calc(b=20,a = 10)# = 左侧的变量的名称称为：关键字参数
print(res)

############################################
#函数的参数传递的内存分析
print('--------------函数的参数传递的内存分析-----------------------')
def fun(arg1,arg2):
    print('arg1= ',arg1)
    print('arg2= ',arg2)
    arg1 = 100
    arg2.append(10)
    print('arg1= ', arg1)
    print('arg2= ', arg2)
n1 = 11
n2 = [22,33,44]
print(n1)
print(n2)
print('---------------------------------')
fun(n1,n2)
print('---------------------------------')
print(n1)
print(n2)
'''在函数调用过程中，进行参数传递
如果是不可变对象，在函数体的修改不会影响实参的值  arg1的修改为100，不会影响n1的值
如果是可变对象，在函数体的的修改会影响到实参的值  arg2的修改，append(10)， 会影响到n2的值
'''
############################################
#函数的多值返回
print('--------------函数的多值返回-----------------------')
def fun(num):
    odd=[]
    even=[]
    for i in num:
        if i%2:
            odd.append(i)
        else:
            even.append(i)
    return odd,even

t = fun([11,22,33,44,55,32,12])
t[0].append(10)
print(t)
for item in t:
    item.sort()
print(t)
'''函数的返回值
(1)如果函数没有返回值[函数执行完毕之后，不需要给调用处提供数据] return可以省略不写
(2)函数的返回值，如果是1个，直接返回类型
3)函数的返回值，如果是多个，返回的结果为元组
'''
#个数可变的位置参数
def fun1(*args):
    print(args)
    return
fun1(12,21,33,41)

#个数可变的关键字参数
def fun2(**args):
    print(args)
    return
fun2(a=1,b=2,c=9)

def fun3(*args1,**args2):
    print(args1)
    print(args2)
    return
fun3(100,21,a=10)
'''pass 
在一个函数的定义过程中，既有个数可变的关键字形参，也有个数可变的位置形参，要求，个数可变的位置形参，放在个数可变的关键字形参之前的
'''

#########################################################################
#递归函数
def fac(num):
    if num == 1:
        return 1
    else:
        return num * fac(num - 1)
print(fac(4))

#斐波那契数列
def fib(n):
    if n==1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
print(fib(6))

#输出这个数列前六位上的数字
lst = []
for i in range(1,11):
    lst.append(fib(i))
print(lst)