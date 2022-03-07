#转义字符
print("hello\rworld")#回车符
print("hello\bworld")#回退一个格

print('http:\\\\www.baidu.com')
print('老师说：\'大家好\'')

#原子符，不希望字符串中的转义字符起作用，就在字符串之前加r或R
print(r'hello\nworld')
#注意事项，最后一个字符不能是反斜杠
#print(r'hello\nworld\')
print(r'hello\nworld\\')
