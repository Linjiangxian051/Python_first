s = '*a**********bc*9876*a*b*c*******'
s = s.strip('abc*')
print(s)


print('---------------------命令行参数---------------------------------')
import getopt
import sys

def usage():
    print("===========")
    print("Usage")
    print("python test_getopt.py -I:127.0.0.1 -p:8888 66 88 or python test_getopt.py --ip=127.0.0.1 --port=8888 66 88")
    print("=======")

def main():
    '''

    python test_getopt.py -i:127.0.0.1 -p:8888
    '''
    options,args = getopt.getopt(sys.argv[1:],'p:i:h',['help','port=','ip='])

    for name,value in options:
        if name in ('-h','--help'):
            usage()
    # for name,value in options:
        if name in ('-i','--ip'):
            print("{1}:{0}".format(value,name))
        if name in ('-p','--port'):
            print("{1}:{0}".format(value,name))

main()

print('---------------------打印分割线---------------------------------')

def print_line(char,times):
    print(char * times)

print_line('*-',100)



print('---------------------高铁售票系统---------------------------------')
import prettytable as pt

#显示坐席
def show_ticket(row_num):
    tb = pt.PrettyTable()
    tb.field_names = ['行号','座位1','座位2','座位3','座位4','座位5']
    for i in range(row_num):
        lst = [f'第{i+1}行','有票','有票','有票','有票','有票']
        tb.add_row(lst)
    print(tb)
#订购坐席
def order_ticket(row_num,row,column):
    tb = pt.PrettyTable()
    tb.field_names = ['行号','座位1','座位2','座位3','座位4','座位5']
    for i in range(row_num):
        if row == (i+1):
            lst = [f'第{i + 1}行', '有票', '有票', '有票', '有票', '有票']
            lst[column] = '已售'
            tb.add_row(lst)
        else:
            lst = [f'第{i + 1}行', '有票', '有票', '有票', '有票', '有票']
            tb.add_row(lst)
    print(tb)


row_num = 13
show_ticket(row_num)
try:
    choose_lst = input('请输入第几行，第几列以英文逗号分割：（12,3）').split(',')
except:
    print('输入有误')
print(choose_lst)
order_ticket(row_num,int(choose_lst[0]),int(choose_lst[1]))


print('---------------------自定义类---------------------------------')
class Car(object):  #父类
    def __init__(self,type,no):
        self.type =type
        self.no = no
    def start(self):
        pass
    def stop(self):
        pass

class Taxi(Car):
    def __init__(self,type,no,company):
        super().__init__(type,no)
        self.company = company
    def start(self):
        print('乘客您好！')
        print('我是{0}出租车公司的，我的车牌号为{1}，请问你要去哪里？'.format(self.company,self.no))
    def stop(self):
        print(f'目的地到了，欢迎乘坐{self.type}车')

class FamilyCar(Car):
    def __init__(self,type,no,name):
        super().__init__(type,no)
        self.name = name
    def start(self):
        print('我是{0}，我的汽车{1}我做主'.format(self.name,self.type))
    def stop(self):
        print('目的地到了，我的车牌{}'.format(self.no))

taxi = Taxi('大众','京A1213','长城')
taxi.start()
taxi.stop()
print('-'*30)
familycar = FamilyCar('比克','京A8888','大朗')
familycar.start()
familycar.stop()


print('---------------------多态---------------------------------')

class Instrument(object):
    def make_sound(self):
        pass

class Erhu(Instrument):
    def make_sound(self):
        print('二胡在演奏')

class Pinao(Instrument):
    def make_sound(self):
        print('钢琴在演奏')

def play(instrument):
    instrument.make_sound()

class Bird():
    def make_sound(self):
        print('小鸟在唱歌')

play(Erhu())
play(Pinao())
play(Bird())


print('---------------------控制台输出带颜色---------------------------------')
print("\033[0;35m对不起\033[0m")#控制台输出带颜色


##########################################################
#进制转换
num = int(input('输入一个整数：'))
print(num,"的二进制数为：",bin(num))
print(str(num)+"的二进制数为："+bin(num))
print("{0}的二进制数为：{1}".format(num,bin(num)))
print("%s的二进制数为：%s" % (num , bin(num)))
print(f"{num}的二进制数为：{bin(num)}")

print("{0}的八进制数为：{1}".format(num,oct(num)))

print(f"{num}的十六进制数为：{hex(num)}")

pwd = input("支付密码：")
if pwd.isdigit():
    print("支付数据合法")
else:
    print("支付数据不合法")

print('-------------------------------------------------------')
import random
price = random.randint(100,500)
print(price)

print('---------------------ASICC值----------------------------------')
x = 98
print(str(x)+"的ASICC值："+chr(x))

print('---------------------千年虫---------------------------------')
year = [98,32,54,56,00,89]  #计算机遇见两个0时只会输出一个
print('原列表：',year)

for index,value in enumerate(year):
    if str(value) != '0':
        year[index] = int('19'+str(value))
    else:
        year[index] = int('200' + str(value))
print(year)

print('---------------------元组---------------------------------')
scores = (("恒大",72),("国安",70),("上港",66),("苏宁",53))
for index,item in enumerate(scores):
    print(index+1,'.',end=' ')
    for score in item:
        print(score)
    print()

print('---------------------猜数---------------------------------')

# import random
#
# def guess(num,random_guess):
#     if num == random_guess:
#         return 0
#     elif num > random_guess:
#         return 1
#     else:
#         return -1
#
# random_guess = random.randint(1,100)
# for i in range(10):
#     num = int(input('输入1-100之间的整数：'))
#     result = guess(num,random_guess)
#     if result == 0:
#         print('猜对了')
#         break
#     elif result > 0:
#         print('大了')
#     else:
#         print('小了')
# else:
#     print('已猜了10次，没机会了')

print('---------------------手动抛出异常---------------------------------')

try:
    score = int(input('输入分数：'))
    if 0 <= score <= 100:
        print('分数为：',score)
    else:
        raise Exception('分数不正确')
except Exception as e:
    print(e)

def is_triangle(a,b,c):
    if a<=0 or b<=0 or c<=0:
        raise Exception('三边必须为正数')
    elif a+b>c and a+c>b and b+c>a:
        print('是三角形')
    else:
        raise Exception(f'a={a},b={b},c={c}，不能构成三角形')
try:
    a = int(input('第一条边：'))
    b = int(input('第二条边：'))
    c = int(input('第三条边：'))
    is_triangle(a,b,c)
except Exception as error:
    print("\033[0;41mError\033[0m:",error)

print('---------------------类的使用---------------------------------')

import math

class Circule(object):
    def __init__(self,r):
        self.r = r
    def get_area(self):
        return math.pi * math.pow(self.r,2)
    def get_perimeter(self):
        return 2 * math.pi * self.r

r = int(input('输入圆的半径：'))
c = Circule(r) #实例化对象
print(c.get_area())
print(c.get_perimeter())

class Student(object):
    def __init__(self,name,age,gender,score):
        self.name =name
        self.age  = age
        self.gender = gender
        self.score  = score
    def show(self):
        print(self.name,self.age,self.gender,self.score)

print('请输入三位学员信息：（姓名#年龄#性别#成绩）')
lst = []
for i in range(3):
    s = input('输入第{}位学员信息：'.format(i+1))
    s_lst = s.split('#')
    #循环创建实例化对象
    stu = Student(s_lst[0],int(s_lst[1]),s_lst[2],float(s_lst[3]))
    lst.append(stu)

for item in lst:
    item.show()




