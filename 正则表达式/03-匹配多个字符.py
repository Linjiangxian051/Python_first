
import re
# *	匹配前一个字符出现0次或者无限次，即可有可无
match_obj = re.match("t.*o","twwwwwwwwwsdo")
if match_obj:
    print(match_obj.group())
else:
    print("匹配失败")
# +	匹配前一个字符出现1次或者无限次，即至少有1次
match_obj = re.match("t.+o","tsfsdfso")
if match_obj:
    print(match_obj.group())
else:
    print("匹配失败")
# ?	匹配前一个字符出现1次或者0次，即要么有1次，要么没有
match_obj = re.match("https?","http")
if match_obj:
    print(match_obj.group())
else:
    print("匹配失败")
# {m}	匹配前一个字符出现m次
match_obj = re.match("ht{,2}ps?","htps")
if match_obj:
    print(match_obj.group())
else:
    print("匹配失败")
# {m,n}	匹配前一个字符出现从m到n次
match_obj = re.match("ht{1,3}ps?","htttps")
if match_obj:
    print(match_obj.group())
else:
    print("匹配失败")
#{m,}：匹配前一个字符最少出现m次
#{,n}：匹配前一个字符最多出现n次
match_obj = re.match("ht{,100}ps?","httttttttttttttttps")
if match_obj:
    print(match_obj.group())
else:
    print("匹配失败")
