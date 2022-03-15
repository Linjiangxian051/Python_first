import math #关于数学运算
print(math,id(math),type(math))
print(dir(math))
print(math.e)
print(math.ceil(9.0001)) #天花板
print(math.floor(9.99999))#地板

#第二种导入方式
from math import pi
print(pi)
#print(sin(20))#未导入的不可使用

#导入自定义模块
import module_calc
print(module_calc.add(10, 20))
print(module_calc.div(10, 20))

#导入包里面的模块
import package.module_B as b_mod #起个别名
from package.module_B import b

print(基础测试.package.module_A.a)
print(b_mod.b)
print(b)
