##################################
#os模块与操作系统有关的一个模块
import os

#os.system('notepad.exe')

#直接调用可执行文件
#os.startfile('C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe')
print(os.getcwd())
print(os.listdir('./'))
#os.mkdir('./wd')
#s.makedirs('A/B/C')
#os.rmdir('./wd')
#os.removedirs('A/B/C')

########################################
#os.path模块操作目录
import os.path

print(os.path.abspath('../TempPython/demo_module_system.py'))
print(os.path.exists('package/module_A.py'))
print(os.path.join('C:\\Users\\linjiang\\Desktop\\','demo2.py'))
print(os.path.split('.././demo2.py'))
print(os.path.splitext('demo_module_system.py'))
print(os.path.basename('C:\\Users\\linjiang\\Desktop\\TempPython\\demo_module_system.py'))
print(os.path.dirname('C:\\Users\\linjiang\\Desktop\\TempPython\\demo_module_system.py'))



