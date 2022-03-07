#####################################################################
#双分支结构
# money = 1000
# s = int(input('请输入取款金额：'))
# if money >= s:
#     money -= s
#     print('取款成功，所剩余额为：',money)
# else:
#     print('余额不足','所剩余额为：',money)
#
# num = int(input('请输入一个整数：'))
# if num % 2 == True:
#     print(str(num)+'是一个奇数')
# else:
#     print(num, '是一个偶数')
#####################################################################
#多分支结构
# score = int(input('请输入分数：'))
#
# if 100 >= score >= 90:
#     print('成绩在90以上')
# elif (score < 90) and (score >= 80) :
#     print('成绩在80以上')
# elif (score < 80) and (score >= 70) :
#     print('成绩在70以上')
# elif (score < 70) and (score >= 60) :
#     print('成绩在60以上')
# else:
#     print('成绩在60以下')
#####################################################################
#嵌套if
# num = int(input('请输入消费金额：'))
# answer = input('是否为会员,请输入yes or no:')
# if answer == 'yes' :
#     if num >= 200:
#         print('打骨折,付款金额为：',num * 0.5)
#     else :
#         print('打九折,付款金额为：',num * 0.9)
# else:
#     if num >= 200 :
#         print('打九五折,付款金额为：',num * 0.95)
#     else:
#         print('不打折，抹个零:',num - num % 10 )
#
#####################################################################
# num_a = int(input('第一个整数：'))
# num_b = int(input('第二个整数：'))
#
# print(str(num_a)+'大于等于'+str(num_b)    if num_a >= num_b  else str(num_a)+'小于'+str(num_b))


