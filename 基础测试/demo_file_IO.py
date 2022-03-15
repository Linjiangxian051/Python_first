



# fp = open('./a.txt','w+')
# print("hello world",file=fp)
# fp.write('psdfsasdaaa')
# print(fp.readlines()) #列表
# fp.close()

################################
#复制图片
# src_file = open('./tb1.jpg','rb')
# target_file = open('./copytb1.jpg','w+b')
#
# target_file.write(src_file.read())
# print('文件指针的位置为：',target_file.tell())
# target_file.seek(0,0)
# print(target_file.read())
# target_file.close()
# src_file.close()

with open('tb1.jpg', 'rb') as src_file:
    with open('copy1tb1.jpg', 'wb') as target_file:
        target_file.write(src_file.read())