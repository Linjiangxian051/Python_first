########################################################
#range函数的使用
# r = range(2,10,2)
# print(list(r)) #2,4,6,8
# print(10 in r)

##################################################
#1到100之间的偶数和
sum = 0
a = 0
while a <= 100:
    if a % 2 == 0:
        sum += a
    a += 1
print(sum,a)