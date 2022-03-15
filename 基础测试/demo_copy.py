class CPU:
    pass

class Disk:
    pass

class Computer:
    def __init__(self,cpu,disk):
        self.cpu  = cpu
        self.disk = disk

#(1)变量的赋值
cpu1 = CPU()
cpu2 = cpu1
print(cpu1,id(cpu1))
print(cpu2,id(cpu2))

#（2）类的浅拷贝
print('---------类的浅拷贝-------------')
disk = Disk()
computer = Computer(cpu1,disk)
#浅拷贝
import copy
computer1 = copy.copy(computer)
print(computer,computer.cpu,computer.disk)
print(computer1,computer1.cpu,computer1.disk)

print('-----------深拷贝-----------')
computer2 = copy.deepcopy(computer)
print(computer,computer.cpu,computer.disk)
print(computer2,computer2.cpu,computer2.disk)
