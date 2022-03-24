import re

# .	匹配任意1个字符（除了\n）
# [ ]	匹配[ ]中列举的字符
# \d	匹配数字，即0-9
# \D	匹配非数字，即不是数字
# \s	匹配空白，即 空格，tab键
# \S	匹配非空白
# \w	匹配非特殊字符，即a-z、A-Z、0-9、_、汉字
# \W	匹配特殊字符，即非字母、非数字、非汉字、非下划线

match_obj = re.match("t.o","tooo\no")

if match_obj:
    print("匹配结果为：",match_obj.group())
else:
    print("匹配失败")#返回值是一个None
#[]:匹配[]中列举的字符
match_obj = re.match("葫芦娃[12]","葫芦娃3122")
if match_obj:
    print("匹配结果为：",match_obj.group())
else:
    print("匹配失败")#返回值是一个None
#匹配银行卡密码中的其中一位
match_obj = re.match("[0123456789][0-9]","012388")
if match_obj:
    print("匹配结果为：",match_obj.group())
else:
    print("匹配失败")#返回值是一个None
match_obj = re.match("[0-9]","5")
if match_obj:
    print("匹配结果为：",match_obj.group())
else:
    print("匹配失败")#返回值是一个None
#\d等价于[0-9]、[0123456789]
match_obj = re.match("\d\d","2a09")
if match_obj:
    print("匹配结果为：",match_obj.group())
else:
    print("匹配失败")#返回值是一个None
# \D:匹配一个非数字的字符
match_obj = re.match("\D\D","90sb")
if match_obj:
    print("匹配结果为：",match_obj.group())
else:
    print("匹配失败")#返回值是一个None
#\s:匹配空白字符
match_obj = re.match("葫芦娃\s[12]","葫芦娃\t2")
if match_obj:
    print("\s匹配结果为：",match_obj.group())
else:
    print("\s匹配失败")#返回值是一个None
#\S:匹配非空白字符
match_obj = re.match("葫芦娃\S[0-9]","葫芦娃\"5")
if match_obj:
    print("匹配结果为：",match_obj.group())
else:
    print("匹配失败")#返回值是一个None
#匹配某网站中密码的其中一位，密码是由字母，数字，下划线组成
match_obj = re.match("[a-zA-Z0-9_]","_")
if match_obj:
    print("匹配结果为：",match_obj.group())
else:
    print("匹配失败")#返回值是一个None
#\w:匹配非特殊字符，如a-z，A-Z，0-9，_，汉字
match_obj = re.match("\w","夏")
if match_obj:
    print("匹配结果为：",match_obj.group())
else:
    print("匹配失败")#返回值是一个None
#\W:匹配特殊字符
match_obj = re.match("[\W\w]","汉字@")
if match_obj:
    print("匹配结果为：",match_obj.group())
else:
    print("匹配失败")#返回值是一个None