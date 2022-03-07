#######################################
#类的创建
class Student: #类名称
    native_pace = '吉林' #类里的变量称为类属性
    def __init__(self,name,age): #初始化实例方法
        self.name = name  #self.name 称为实例属性
        self.age  = age

    #实例方法，实例方法需要将类实例化后调用，如果使用类直接调用实例方法,需要显式地将实例作为参数传入。
    def eat(self):
        print('学生再吃饭')
    def func_a(): #只能通过类去调用这个方法，如果使用实例调用这个方法会引发异常。
        print('不加self参数的实例方法')
    #静态方法
    @staticmethod
    def method():
        print('使用了staticmethod，所以说静态方法')

    #类方法
    @classmethod
    def cm(cls):
        print('使用了classmethod，所以是类方法')
#######################################
#创建类的对象，即对Student类实例化
stu1 = Student('张三',20)
stu1.eat()
print(stu1.name)
print(stu1.age)

print('---------------------')
Student.eat(stu1)#类名.方法名（类的对象）-->实际上就是方法定义处的self，实例方法需要将类实例化后调用，如果使用类直接调用实例方法,需要显式地将实例作为参数传入。

print('---------------------')
stu2 = Student('李四',30)
print(stu1.native_pace)
print(stu2.native_pace)
stu1.native_pace = '济南'
Student.native_pace = '天津'
print(stu1.native_pace)
print(stu2.native_pace)

stu1.native_pace = '济南'

stu3 = Student('王五',99)
print(stu3.native_pace)
#print(Student.cm())
stu1.cm()
stu1.method()

#stu1.func_a() #报异常
Student.func_a()