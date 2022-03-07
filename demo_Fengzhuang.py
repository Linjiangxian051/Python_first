class Student:
    def __init__(self,name,age):
        self.name = name
        self.__age = age
    def show(self):
        print(self.name,self.__age)

stu = Student('张三',20)
stu.show()
#在类的外部使用name与age
print(stu.name)

print(dir(stu))
print(stu._Student__age) #加了两个下划线的类属性，可以通过dir获取到，然后使用

