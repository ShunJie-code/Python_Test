"""
__new__ 用于创建对象
__init__ 用于初始化对象
__str__ 默认输出对象的内存地址S
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return '这是一个人类，有name和age两个实例属性'

    @staticmethod
    def eat():
        print("人吃五谷杂粮")


per = Person('xsj', 20)
print(dir(per))  # 除了eat 以外其他的方法都是父类object的方法
print(per)       # 自动调用了__str__，默认输出地址
