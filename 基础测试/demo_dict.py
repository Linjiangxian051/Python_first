######################################################
#字典的创建方式
scores = {'张三':100,'李四':90,'王五':12}
print(scores)

students = dict(name='jack',age = 20)
print(students)

'''空字典'''
d = {}
######################################################
#字典的获取
print('---------------字值的获取,增，删，改----------------------')
print('张三',scores['张三'])

print(scores.get('三',90))

scores['Jack'] = 88
print(scores)

del scores['王五']
print(scores)

scores['Jack'] = 110
print(scores)

scores.pop('Jack')
print(scores)

#获取所有键key
keys = scores.keys()
print(keys,type(keys))
list_keys = list(keys) #转换成列表
print(list_keys[1])

#获取所有值value
value = scores.values()
print(value,type(value))
list_value = list(value)
print(list_value)

#获取所有键值对
items = scores.items()
print(items,type(items))
list_items = list(items)
print(list_items)   #转换后的列表元素是由元组组成

#遍历
scores['Jack'] = 20
print('#遍历')
for item in scores:
    print(item,type(item))
    print(scores[item],scores.get(item))

#字典生成公式
print('-------------字典生成式-----------------')
items  = ['Fruits','Books','Others']
prices = [96,23,32]
d = {item.upper():price for item,price in zip(items,prices)}
print(d)

'''
zip()是Python的一个内建函数，它接受一系列可迭代的对象作为参数，将对象中对应的元素打包成一个个tuple（元组），
然后返回由这些tuples组成的list（列表）。若传入参数的长度不等，则返回list的长度和参数中长度最短的对象相同。
也就是说，该函数返回一个以元组为元素的列表，其中第 i 个元组包含每个参数序列的第 i 个元素。
返回的列表长度被截断为最短的参数序列的长度。只有一个序列参数时，它返回一个1元组的列表。
没有参数时，它返回一个空的列表。利用*号操作符，可以将list unzip（解压）.
'''
items  = ['one','two','three']
prices = [1,2,3]
a = zip(items,prices)
print(a)
for i in a:
    print(i) #遍历通过zip的a后，a会丢失????????????????????????????????????????????????????
print(a)

for j in a:
    print(j+'\n')

d = dict(a)
print(d)

a = [('Fruits', 96),('Books', 23),('Others', 32)]

print(a)
for i in a:
    print(i)
d = dict(a)
print(d)
# d = dict(a)
# print(d)
# d = dict(zip(items,prices))
# for i in d:
#     print(i,d[i])