class Animal(object):
    def eat(self):
        print('动物吃东西')
class Dog(Animal):
    def eat(self):
        print('狗吃肉')
class Cat(Animal):
    def eat(self):
        print('猫吃鱼')
class Person(object):
    def eat(self):
        print('任吃饭')
def fun(animal):#匿名对象
    animal.eat()

fun(Dog())#等价于animal = Dog（），动态实例化
fun(Cat())
fun(Person())
c =Cat()
c.eat()
Cat.eat(self='1')