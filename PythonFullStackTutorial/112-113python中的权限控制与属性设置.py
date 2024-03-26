"""
面向对象的三大特征
封装、继承、和多态
保护 单下划线
"""


class Student:
    def __init__(self, name, age, gender):
        self._name = name  # 受保护的属性
        self.__age = age   # 私有的属性
        self.gender = gender

    # 把方法当成属性用
    @property
    def age(self):
        return self.__age

    def _func1(self):  # 受保护的方法
        print('子类及本身可以访问')

    def __func2(self):  # 私有方法
        print('只有定义的类可以访问')

    def show(self):
        self._func1()
        self.__func2()
        print(self._name)
        print(self.__age)


stu = Student('xsj', 20, '男')
print(stu._name)  # 可以输出，但是提示：不建议这么使用
print(stu._Student__age)
print(stu.gender, stu.age)
