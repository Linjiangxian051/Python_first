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