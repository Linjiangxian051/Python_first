
import os.path
import time

filename = 'student.txt'

def main():
    while True:
        menu()
        choice = int(input('请选择：'))
        if choice in [0,1,2,3,4,5,6,7] :
            if choice == 0:
                anwser = input('确认退出系统吗？y/n\t\t')
                if anwser == 'y' or anwser == 'Y':
                    print('Thank you!')
                    break #退出系统
                else:
                    continue #跳出本次的循环体
            elif choice == 1:
                insert()
            elif choice == 2:
                search()
            elif choice == 3:
                delete()
            elif choice == 4:
                modify()
            elif choice == 5:
                sort()
            elif choice == 6:
                total()
            elif choice == 7:
                show()

def menu():
    print('===============================学生信息管理系统=====================================')
    print('-------------------------------功能菜单-------------------------------------------')
    print('\t\t\t\t\t\t0.Quit')
    print('\t\t\t\t\t\t1.录入学生信息')
    print('\t\t\t\t\t\t2.查找学生信息')
    print('\t\t\t\t\t\t3.删除学生信息')
    print('\t\t\t\t\t\t4.修改学生信息')
    print('\t\t\t\t\t\t5.排序')
    print('\t\t\t\t\t\t6.统计所有学生信息')
    print('\t\t\t\t\t\t7.显示学生信息')
    print('-----------------------------------------------------------------------------------')

def insert():
    stu_list = []
    while True:
        id   = input('输入学生id：')
        if not id:
            break
        name = input('输入学生姓名：')
        if not name:
            break
        try:
            english = int(input('输入英语成绩：'))
            python  = int(input('输入Python成绩：'))
        except:
            print('输入无效，成绩信息不是整数类型，请重新输入')
            continue
        stu_infodict = {'id':id,'name':name,'english':english,'python':python}
        stu_list.append(stu_infodict)
        anwser = input('是否继续输入：y/n\n')
        if anwser == 'y' or anwser == 'Y':
            continue
        else:
            break
    save(stu_list)
    print('学生信息录入完毕！！！')

def save(lst):
    file = open(filename,'a',encoding='utf-8')
    for item in lst:
        file.write(str(item)+'\n')
    file.close()

def search():
    student_query =[]
    while True:
        id = ''
        name = ''
        flag = False
        if os.path.exists(filename):
            mode = input('按ID查找请输入1，按姓名查找请输入2：')
            if mode == '1':
                id = input('请输入学生ID：')
            elif mode == '2':
                name = input('请输入查找的学生姓名：')
            else:
                print('输入有误，请重新输入！！！')
                search()
            with open(filename,'r',encoding='utf-8') as rfile:
                stu_list = rfile.readlines()
            if stu_list:
                for item in stu_list:
                    d = dict(eval(item))
                    if  mode == '1':
                        if d['id'] == id:
                            student_query.append(d)
                            flag = True
                    elif mode == '2':
                        if d['name'] == name:
                            student_query.append(d)
                            flag = True
                #if len(student_query) != 0
                if flag:
                    show_student(student_query)
                    student_query.clear()
                else:
                    print(f'id为：{id}不存在' if mode == '1' else f'name为:{name}不存在' )
                anwser = input('是否继续查询？y/n\n')
                if anwser == 'y' or anwser == 'Y':
                    continue
                else:
                    break
            else:
                print('无学生信息')
        else:
            print('No exist')
            break

def show_student(lst):
    #print(lst)
    #定义标题显示格式
    format_title = '{0:^6}\t{1:^12}\t{2:^8}\t{3:^8}\t{4:^8}'
    print(format_title.format('ID','姓名','英语成绩','python成绩','总成绩'))
    #定义内容显示格式
    format_data = '{0:^6}\t{1:^12}\t{2:^8}\t{3:^8}\t{4:^8}'
    for item in lst:
        print(format_data.format(item.get('id'),
                                 item.get('name'),
                                 item.get(('english')),
                                 item.get('python'),
                                 int(item.get('english'))+int(item.get('python'))
                                 ))

def delete():
    show()
    while True:
        d = {}
        delete_id = input('输入删除的id：')
        if not delete_id:
            break
        if os.path.exists(filename):
            with open(filename,'r',encoding='utf-8') as student_txt:
                stu_list = student_txt.readlines() #加双引号的字符串列表
        else:
            stu_list = []
        flag = False
        if stu_list:
            with open(filename,'w',encoding='utf-8') as wfile:
                for stu_infodict in stu_list:
                    d = dict(eval(stu_infodict))#对参数进行解析和计算，在此处是为了去掉字符串的双引号
                    if d['id'] != delete_id:
                        wfile.write(str(d)+'\n')
                    else:
                        flag = True
                if flag:
                    print(f'id为{delete_id}的学生信息已删除')
                else:
                    print(f'id为{delete_id}的学生信息不存在')
        else:
            print('无学生信息')
            break
        show()
        anwser = input('是否继续删除学生信息：y/n\t\t')
        if anwser == 'y' or anwser == 'Y':
            continue
        else:
            break

def modify():
    while True:
        show()
        d = {}#空字典
        flag = False
        if os.path.exists(filename):
            with open(filename,'r',encoding='utf-8') as rfile:
                stu_list = rfile.readlines()
            #print(stu_list)
        else:
            print('No exist')
            break
        if stu_list:
            with open(filename,'w',encoding='utf-8') as wfile:
                while True:
                    try:
                        modify_id = int(input('输入修改学生的id： '))
                        break
                    except:
                        print('输入非法，请重新输入！！！')
                        continue
                for stu_infodict in stu_list:
                    d = dict(eval(stu_infodict))
                    if int(d['id']) == modify_id:
                        while True:
                            try:
                                d['id']  = input('New id     :')
                                d['name'] = input('New name   :')
                                d['english'] = int(input('New English:'))
                                d['python'] = int(input('New Python :'))
                        #     if not d['id']:
                        #         print('输入非法，请重新输入！！！')
                        #         continue
                        #     else:
                        #         break
                        # while True:
                        #     d['name']  = input('New name   :')
                        #     if not d['name']:
                        #         print('输入非法，请重新输入！！！')
                        #         continue
                        #     else:
                        #         break
                        # while True:
                        #     try:
                        #         d['english'] = int(input('New English:'))
                        #         break
                        #     except:
                        #         print('输入非法，请重新输入！！！')
                        #         continue
                        # while True:
                        #     try:
                        #         d['python']  = int(input('New Python :'))
                        #         break
                            except:
                                print('输入非法，请重新输入！！！')
                                continue
                            else:
                                break
                        wfile.write(str(d)+'\n')
                        flag = True
                        print('id为{0}的学生信息已修改完毕，新id为：{1}'.format(modify_id,d['id']))
                    else:
                        wfile.write(str(d) + '\n')
                if flag:
                    anwser = input('是否继续修改学生信息：y/n\t\t')
                    if anwser == 'y' or anwser == 'Y':
                        continue
                    else:
                        break
                else:
                    print(f'学生信息表中不存在id为：{modify_id}的学生')
        else:
            print('无学生信息')
            break


def sort():
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
            list_student = rfile.readlines()
        if list_student:
            student_new = []
            for item in list_student:
                d = dict(eval(item))
                student_new.append(d)
        else:
            print('无学生信息')
            return
        asc_or_dasc = bool(input('请选择（0.升序  1.降序）'))
        mode = input('请选择排序方式（1.English成绩 2.Python成绩 3.Total成绩）')
        if mode == '1':
            student_new.sort(key=lambda x:int(x['english']),reverse=asc_or_dasc)
        elif mode == '2':
            student_new.sort(key=lambda x:int(x['python']),reverse=asc_or_dasc)
        elif mode == '3':
            student_new.sort(key=lambda x: int(x['english']) + int(x['python']),reverse=asc_or_dasc)
        show_student(student_new)
    else:
        print('No exist')
def total():
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
            list_student = rfile.readlines()
        if list_student:
            print('已录入学生人数为：'+str(len(list_student))+'位')
            for item  in list_student:
                d = dict(eval(item))
                print('{0}\t{1}'.format(d.get('id'),d.get('name')))
        else:
            print('未录入学生信息')
    else:
        print('No exist')
    time.sleep(5)
def show():
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
            list_student = rfile.readlines()
        if list_student:
            lst = []
            #print(list_student)
            for item in list_student:
                item = eval(item)#由于readlines（）函数的特性：将每一行作为独立的字符串对象放入列表中，故需要去掉双引号“”
                lst.append(item)
            show_student(lst)

        else:
            print('未录入学生信息')
    else:
        print('No exist')
    time.sleep(2)


if __name__ == '__main__':
    main()