"""
浅拷贝
深拷贝
"""
import copy


class Cpu:
    pass


class Disk:
    pass


class Computer:
    def __init__(self, com_cpu, com_disk):
        self.cpu = com_cpu
        self.disk = com_disk


cpu = Cpu()
disk = Disk()

com = Computer(cpu, disk)

# 1 对象赋值仅仅只是一个别名
com1 = com
# com 和 com1 是一个地址
print(com, 'com 子对象的内存地址', com.cpu, com.disk)
print(com1, "com1 子对象内存地址", com1.cpu, com1.disk)

# 2 浅拷贝
com2 = copy.copy(com)
print(com2, "com2 子对象内存地址", com2.cpu, com2.disk)


# 3 深拷贝
com3 = copy.deepcopy(com)
print(com3, "com3 子对象内存地址", com3.cpu, com3.disk)
