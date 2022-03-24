import re

# #  |	匹配左右任意一个表达式
# (ab)	将括号中字符作为一个分组
# \num	引用分组num匹配到的字符串
# (?P<name>)	分组起别名
# (?P=name)	引用别名为name分组匹配到的字符串

#水果列表
fruit_list = ['apple','banana','orage','pear','peach']

for i in range(len(fruit_list)):
    match_obj = re.match("apple|pear",fruit_list[i])
    if match_obj:
        print("{0}是我想要的".format(match_obj.group()))
    else:
        print(f"{fruit_list[i]}不是我想要的")
    print()

#需求：匹配出163、126、qq等邮箱
# \.: 表示对正则表达式里面的.进行了转义，变成了一个普通点，只能匹配.字符
match_obj = re.match("[a-zA-Z0-9_]{4,20}@(163|126|sina|qq|yahoo)\.com","hello@qq.com")
if match_obj:
    # 获取整个匹配的数据，如果使用分组数的话，默认是0
    print(match_obj.group(0))
    #获取分组数据
    print(match_obj.group(1))
else:
    print("匹配失败")


#需求: 匹配qq:10567这样的数据，提取出来qq文字和qq号码
match_obj = re.match("(qq):([1-9]\d{4,10})","qq:109865554")
if match_obj:
    # 获取整个匹配的数据，如果使用分组数的话，默认是0
    print(match_obj.group(0))
    #获取分组数据
    print(match_obj.group(1))
    print(match_obj.group(2))
else:
    print("匹配失败")

#需求：匹配出<html>hh</html>
match_obj = re.match("<[a-zA-Z1-6]+>.*</[a-zA-Z1-6]+>","<html>hh</div>")
if match_obj:
    print(match_obj.group())
else:
    print("匹配失败")

match_obj = re.match("<([a-zA-Z1-6]+)>.*</\\1>","<html>dasd</html>")
if match_obj:
    print(match_obj.group())
else:
    print("匹配失败")

#需求：匹配出<html><h1>www.itcast.cn</h1></html>
match_obj = re.match("<([a-zA-Z1-6]+)><([a-zA-Z1-6]+)>.*</\\2></\\1>","<html><div>adad</div></html>")
if match_obj:
    print(match_obj.group())
else:
    print("匹配失败")
#(?P<name>) (?P=name)
match_obj = re.match("<(?P<name1>[a-zA-Z1-6]+)><(?P<name2>[a-zA-Z1-6]+)>.*</(?P=name2)></(?P=name1)>","<html><h1>www.itcast.cn</h1></html>")
if match_obj:
    print(match_obj.group())
else:
    print("匹配失败")