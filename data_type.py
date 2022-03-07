#整数可以表示为十进制、二进制、八进制、十六进制
print("十进制",1121)
print('二进制',0b110)
print('八进制',0o721)
print('十六进制',0xef1)


#浮点数类型
n1 = 1.1
n2 = 2.2
print(n1+n2)
#解决方案
from decimal import Decimal
print(Decimal('1.1') + Decimal('2.2'))


#布尔类型
f1 = True  #1
f2 = False #0
print(f1+1)
print(f2+1)

#字符串类型
str1 = '''Python
        
        苦大'''
print(str1)