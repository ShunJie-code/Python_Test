"""
可以后续绑定属性和方法
"""


class Student:
    school = "北大"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print("我的名字{}，今年{}岁".format(self.name, self.age))

    @staticmethod
    def sm():
        print("这是一个静态方法，不能用实例属性和实例方法")

    @classmethod
    def cm(cls):
        print("这是一个类方法，不能用实例属性和实例方法")
        print("但可用类属性，我的学校是{}".format(cls.school))


def introduce():
    print("我是一个普通的函数，被动态绑定为stu1的方法")


def test1():
    stu1 = Student("hh", 10)
    stu2 = Student("xsj", 18)
    # 只有stu2有这个属性
    stu2.gender = '男'
    print(stu2.gender)
    # print(stu1.gender)
    # 不能加括号，直接赋值
    stu1.fun = introduce
    stu1.fun()


test1()
