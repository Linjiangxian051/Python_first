####################################
#继承
# class Person(object): #Person继承object类
#     def __init__(self,name,age):
#         self.name = name
#         self.age  = age
#     def info(self):
#         print('姓名：{0}，年龄{1}'.format(self.name,self.age))
# #定义子类
# class Student(Person):
#     def __init__(self,name,age,score):
#         super().__init__(name,age) #super:实现了在子类中调用父类的方法
#         self.score = score
#
# #测试
# stu = Student('Jack',20,'1001')
# print(stu.name)
# stu.info()
####################################
#方法重写
# class Person(object):
#     def __init__(self,name,age):
#         self.name = name
#         self.age  = age
#     def info(self):
#         print('姓名:{0},年龄：{1}'.format(self.name,self.age))
# class A:
#     pass
#
# #定义子类
#
# class Student(Person,A):
#     def __init__(self,name,age,score):
#         super().__init__(name,age)
#         self.score = score
#     def info(self):
#         super().info()
#         print('学号:{0}'.format(self.score))
#     def __str__(self):#用于返回对于对象的描述，可以查看对象的信息，所以经常重写str方法
#         return '我的姓名是：{0},年龄是：{1}'.format(self.name,self.age)
# class B(A):
#     pass
#
# #测试
# stu = Student('Jack',20,'101')
# stu.info()
# print(dir(stu))#查看指定对象的所有属性
# print(stu)#默认会调用__str__()这样的方法
# #特殊属性
# print(stu.__dict__)#查看实例对象的属性的字典
# print(Student.__dict__)#查看类对象的属性和方法的字典
# print('-------------------------------------------------------------')
# print(stu.__class__)#输出对象所属的类
# print(Student.__bases__)#输出Student类的父类类型的元组
# print(Student.__base__)#输出Student类的父类类型的第一个,即基类
# print(Student.__mro__) #输出Student类的层次结构
# print(A.__subclasses__())#查看父类的子类列表
################################################################
#特殊方法
print('-----------特殊方法--------------')
class Student(object):
    def __init__(self,name):
        self.name = name
    def __add__(self, other): #重写add方法实现自定义对象相加
        return self.name + other.name
    def __len__(self): #重写len方法
        return len(self.name)

stu1 = Student('张三')
stu2 = Student('李四')
s = stu1 + stu2 #实现了两个对象的加法运算，在Student类中，重写了add方法
print(s)
s1 = stu1.__add__(stu2)
print(s1)
print('--------------------------------------------------')
lst = [11,22,33,44]
print(len(lst))#计算列表长度的内置函数
print(lst.__len__())#特殊方法

print(stu1.__len__())#调用重写后的len方法

