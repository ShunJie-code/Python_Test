"""
面向对象的三大特征
封装、继承、和多态
保护 单下划线
"""

class Student:
    def __init__(self, name, age, gender):
        self._name = name
        self.__age = age
        self.gender = gender

    def _func1(self):
        print('子类及本身可以访问')

    def __func2(self):
        print('只有定义的类可以访问')
