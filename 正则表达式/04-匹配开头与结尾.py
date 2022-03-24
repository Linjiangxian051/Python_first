import re

#^ 匹配字符串开
#$ 匹配字符串结尾
match_obj = re.match("^\d.*[\w]$","1i")
if match_obj:
    print(match_obj.group())
else:
    print("匹配失败")

#[^aeiou] : 除了指定的字符aeiou都匹配
match_obj = re.match("[^aeiou].{3}[^47]$","1sad6as")
if match_obj:
    print(match_obj.group())
else:
    print("匹配失败")
