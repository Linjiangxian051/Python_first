############################
#字符串的查找
s = 'heLlo hellO'
print(s.index('lo'))
print(s.rindex('lo'))

print(s.find('e'))
print(s.rfind('lo'))

print(s.upper())
print(s.lower())
print(s.swapcase())
print(s.capitalize())
print(s.title())
############################
#字符串的内容对齐
s1 = 'hello,python'
print(s1.center(20,'-'))
print(s1.ljust(20))
print(s1.zfill(20))
print('-8910'.zfill(8))
############################
#字符串的分割
s2 = 'hello world Python'
lst = s2.split(sep='o',maxsplit=2)
print(lst)
############################
#字符串的判断
s3 = '\t\n\r'
print(s3)
print(s3.isspace())
张三 = 'pyh'
print(张三)
print('张三'.encode('UTF-8').isalpha())

print('壹贰'.isnumeric())#True
#替换
s4 = 'hello,Python'
print(s4.replace('Python','Java'))
print(s4.replace('o','Java',1))

t = ('Wangwu','Hello')
print(t)
print('.'.join(t))
print('*'.join('Python'))

#切片
s4 = 'hello,Python'
print(s4[1])
s41 = s4[:5]
s42 = s4[6:]
newstr = s41 + '!' +s42
print(newstr)
#############################################
#格式化字符串
print('----------格式化字符串----------')
name = '张三'
age = 98
print('my name is %s,%d years old' % (name,age))

print('my name is {0},{1} years old'.format(name,age).ljust(40).capitalize())

print(f'my name is {name},{age} years old')
print('----------------对齐显示字符串-----------------')
print('{0:^7.3}'.format(3.1412)) #^7.3: ^7表示指定显示字符串宽度为7，居中对齐格式(<:左对齐，z>:右对齐)，指定的宽度小于实际要显示的字符宽度时则显示原字符串；.3表示是一个保留三位数
print('{0:.3f}'.format(3.1415926))#.3f表示保留三位小数
#############################################
#字符串编码解码
print('----------字符串编码解码----------')
s = '天涯共此时'
#编码
print(s.encode(encoding='GBK'))
byte = s.encode(encoding='GBK')

print(byte.decode(encoding='GBK'))