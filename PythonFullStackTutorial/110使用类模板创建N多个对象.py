class Student:
    school = "北大"

    # 初始化方法
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 实例方法
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
    stu1 = Student("xsj", 18)
    stu2 = Student("x", 28)
    stu3 = Student("s", 38)
    stu4 = Student("j", 48)
    ls = [stu1, stu2, stu3, stu4]
    print(type(stu1), type(ls))
    for item in ls:
        item.show()


test1()
