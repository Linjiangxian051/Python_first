#集合的创建
s = {'Python','hello',90,90}
print(s,type(s),id(s))

s1 = set(range(6))
print(s1)

s2 =set([1,2,3,4,5,6,1])
print(s2)

s3 = set(('Python','hello',90)) #集合中的元素是无序的
print(s3)

s4 = set('python')
print(s4) #{'p', 't', 'o', 'h', 'y', 'n'}

s5 = set({12,3,2,32,2,31,44})
print(s5)
for item in s5:
    print(item)
###########################################################
#集合的相关操作
print('---------集合的增，删--------------------')
s ={10,20,30,40,50}
#增加
s.add(90)
print(s)
s.update({100,99,98})
print(s)
s.update([111,22,333])
print(s)
s.update(('python','world',90))
print(s)
#删除
s.remove(99)
print(s)
s.discard('ppp')
print(s)
s.pop()
print(s)
s.pop()
print(s)
s.pop()
print(s)
s.pop()
print(s)
s.clear()#清空
print(s)
###########################################################
#集合间的关系
s1 = {10,20,40,30,50}
s2 = {40,20,50,30,60}
#相等
print(s1 == s2)  #判断两个集合里元素是否相同
#子集
print(s1.issubset(s2)) #理解为：s1是s2的子集吗？ False
print(s2.issubset(s1))
#超集
print(s1.issuperset(s2))
print(s2.issuperset(s1))
#有无交集
print(s1.isdisjoint(s2)) #两集合是否不存在相同的元素
###########################################################
#集合间的数学操作
#求交集
print(s1.intersection(s2))
print(s1 & s2)

#求并集
print(s1.union(s2))
print(s1 | s2)

#求差集
print(s1.difference(s2))
print(s1 - s2)

#求对称差集
print(s1.symmetric_difference(s2))
print(s1 ^ s2)