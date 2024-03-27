class Father1:
    def __init__(self, name):
        self.name = name

    def show1(self):
        print("父类1中的方法，name = {}".format(self.name))


class Father2:
    def __init__(self, age):
        self.age = age

    def show2(self):
        print("父类2中的方法，age = {}".format(self.age))


class Son(Father1, Father2):
    def __init__(self, name, age, gender):
        # 需用两个父类的初始化方法
        Father1.__init__(self, name)
        Father2.__init__(self, age)
        self.gender = gender


son = Son('xsj', 18, '男')
son.show1()
son.show2()
