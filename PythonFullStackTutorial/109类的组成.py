"""
类属性 : 方法外的变量
实例属性 ：__init__ 中 self 打点的变量
实例方法：自带参数self
静态方法：@staticmethod
类方法：@classmethod
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


def test1():
    stu = Student('xsj', 18)
    # 实例属性和类属性
    print(stu.name, Student.school)
    # 实例方法
    stu.show()
    # 类方法和静态方法，都可以通过类名打点调用
    Student.cm()
    Student.sm()


test1()
