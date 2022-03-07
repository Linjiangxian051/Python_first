lst = ['hello','world',98]
print(id(lst))
print(type(lst))
#lst[1] = 'OK!'
print(lst[1])
print(lst.index(98,1,3))#在索引1--2中查找，不包括3
##############################################################################
#列表中元素切片操作
lst1 = [10,20,30,40,50,60,70,80]
#start = 1 : stop = 6 : step = 1
print(lst1[1:6:1])
print(lst1[:6:2])
print(lst1[0::2])
#遍历列表
for item in lst1:
    print(item,end='\t')
print()
lst1.append(90)
print(lst1)
lst2 = [100,110,120]
lst1.extend(lst2)
print(lst1)
lst1.insert(0,0)
print(lst1)
#切片
lst1[1:] = lst2
print(lst1)
##########################################################################
#列表的删除操作
lst1 = [10,20,30,40,50,60,70,80]
print(lst1)

lst1.remove(10)#元素
print(lst1)

lst1.insert(0,10)
print(lst1)

lst1.pop(1)#位置
print(lst1)

lst3 = lst1[1:3:1]
print(lst3)

lst1[1:3] = []
print('切片后的列表',lst1)

lst3.clear()#清空
print(lst3)
del lst3 #删除
#print(lst3)

##########################################################################
#列表的修改
print('----------列表修改--------------')
lst1 = [10,20,30,40,50,60,70,80]
#切片
lst1[1:3] = [200,300]
print(lst1)

##########################################################################
#列表的排序
print('----------列表排序--------------')
lst = [44,22,11,55,77,66,99,88,33]
print('排序前的列表',lst,id(lst))
new_list = sorted(lst,reverse=True)
print('内置函数sorted()排序产生的新列表对象',new_list)
lst.sort(reverse=True)
print('sort降序排序后的列表',lst,id(lst))

##########################################################################
#列表的生成式
print('----------列表生成式--------------')
lst = [i for i in range(2,11,2)]
print(lst)
print(1 in lst)