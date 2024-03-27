"""
python 中的一个子类可以继承N多个父类
一个父类也可以有N多个子类
如果一个类没有继承任何类，则默认继承object类

拥有父类的公有成员和受保护成员
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print("大家好，我是{}，今年{}岁".format(self.name, self.age))


class Student(Person):
    def __init__(self, name, age, stu_no):
        super().__init__(name, age)  # 调用父类的方法赋值
        self.stu_no = stu_no


class Doctor(Person):
    def __init__(self, name, age, department):
        super().__init__(name, age)  # 调用父类的方法赋值
        self.department = department


stu = Student('xsj', 18, 201966)
stu.show()

doctor = Doctor('hui', 28, '骨科')
doctor.show()
