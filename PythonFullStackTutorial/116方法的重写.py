"""
9-12
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

    def show(self):
        super().show()     # 调用父类的show方法
        print("我是学生，我的学号是{}".format(self.stu_no))


class Doctor(Person):
    def __init__(self, name, age, department):
        super().__init__(name, age)  # 调用父类的方法赋值
        self.department = department

    def show(self):
        # super().show()
        print("{}是医生，我的科室是{}".format(self.name, self.department))


stu = Student('xsj', 18, 201966)
stu.show()

doctor = Doctor('慧慧', 28, '骨科')
doctor.show()
