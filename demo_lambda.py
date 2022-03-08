test = lambda x,y:x+y

print(test(10,20))

greater = lambda x,y: x if x>y else y
print(greater(20,23))

result = (lambda x,y:x if x>y else y)(89,82)#直接调用
print(result)