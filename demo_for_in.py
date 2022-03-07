for item in "Python":  #第一次取出来的是P，将P赋值item，将item的值输出
    print(item)

#range()产生一个整数序列，该序列也是一个可迭代对象
for i in range(10):
    print(i)
#如果在循环体中不需要使用到自定义变量，可将自定义变量写为下划线“_”
for _ in range(5):
    print('人生苦短')
sum  = 0
i = 0
for i in range(1,101):
    if not bool(i%2):
        sum += i
print(sum)
#######################################################################
#for循环产生100-999之间的水仙花数
i = 0
num_a = num_b = num_c =0
for i in range(100,1000):
    num_a = i // 100
    num_b = i % 100 // 10
    num_c = i % 10
    #print('i = ',i,'num_a = ',num_a,'num_b = ',num_b,'num_c = ',num_c)
    if i == (num_a ** 3 + num_b ** 3 + num_c ** 3):
        print(i)
        break
##########################################################################
#输出1--50之间所有5的倍数
for item in range(1,51):
    if item % 5:
        continue
    print(item)
##########################################################################
#银行密码
#print('')
for i in range(3):
    pwd = input('请输入密码：')
    if pwd == '8888':
        print('密码正确')
        break
    else:
        print('密码错误，重新输入')
else:
    print('对不起，三次均输入错误')
##########################################################################
#嵌套循环：输出九九乘法表
sum = 0
for i in range(1,10):
    for j in range(1,10):
        if i < j:
            break
        sum = i*j
        print(j,'*',i,'=',sum,end='\t')
    print()