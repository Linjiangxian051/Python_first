import re

match_obj = re.match("lo","lohellolllo")
result = match_obj.group()#返回的是一个匹配对象
print(result)