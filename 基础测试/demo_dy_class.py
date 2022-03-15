class Student:
    def __init__(self,name,age):
        self.name = name
        self.age  = age
    def eat(self):
        print(self.name+'在吃')

#实例对象
stu1 = Student('张三',20)
stu2 = Student('李四',40)
print(id(stu1))
print(id(stu2))

stu2.gender = '女' #为实例对象stu2动态绑定属性
print(stu1.name,stu1.age)
print(stu2.name,stu2.age,stu2.gender)

print('-----------动态绑定方法---------')
def show():
    print('定义在类之外的，称为函数')
stu1.show = show

stu1.show()