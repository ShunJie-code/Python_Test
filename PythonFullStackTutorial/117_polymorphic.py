"""
117 多态
"""


class Person:
    @staticmethod
    def eat():
        print("人吃五谷杂粮")


class Cat:
    @staticmethod
    def eat():
        print("猫喜欢吃鱼")


class Dog:
    @staticmethod
    def eat():
        print("狗喜欢啃骨头")


def fun(obj):
    """
    :param obj: 动态决定调用哪个对象
    :return:
    """
    obj.eat()


def test1():
    string1 = '年月日'
    print(string1[0], string1[1], string1[2])
    temp = input("不妨猜一下我想的是哪一个数字：")
    guess = int(temp)

    if guess == 8:
        print("Yes")


def test2():
    person = Person()
    cat = Cat()
    dog = Dog()
    # python中的多态，不关心对象的数据类型，只关心对象是否有同名方法
    fun(person)
    fun(cat)
    fun(dog)


if __name__ == "__main__":
    test2()
