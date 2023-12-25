"""
5 函数和代码复用
"""


# 5.1 函数的定义、调用过程
def fact(n):
    s = 1
    for i in range(1, n + 1):
        s *= i
    return s


def test2():
    # 5.1.3 lambda 函数主要用作一些特定函数或方法的参数
    f = lambda x, y: x + y
    print(type(f))
    print('f(10, 12) = {}'.format(f(10, 12)))


# 5.2.1 可选参数和可变参数数量
def fact_divided(n, m=1):
    # 可选参数传递
    s = 1
    for i in range(1, n + 1):
        s *= i
    # 双斜杠表示整除,返回元组
    return s // m, n, m


def fact_multiply(n, *b):
    s = 1
    for i in range(1, n + 1):
        s *= i
    for item in b:
        s *= item
    return s


def test1():
    print("5！= {}".format(fact(5)))
    print("4！= {}".format(fact(4)))
    print("4！/ 2 = {}".format(fact_divided(4, 2)))
    print("5！/ 1 = {}".format(fact_divided(5)))
    print("10！/ 5 = {}".format(fact_divided(10, 5)))
    print("10！* 3 = {}".format(fact_multiply(10, 3)))
    print("3！* 5 * 4 = {}".format(fact_multiply(3, 5, 4)))


def func(x1, y1, z1, x2, y2, z2):
    print(x1, x2, y1, y2, z1, z2)


def func1(a, b):
    return b, a * b


# 5.2.2 参数的位置和名称传递
def test3():
    func(1, 2, 3, 4, 5, 6)
    func(x2=4, x1=1, y2=5, y1=2, z1=3, z2=6)
    s = func1('hello~', 2)
    func2('c')
    print(ls)
    # 5.2.3 函数的返回值
    print(s, type(s))


ls = ['f', 'F']


def func2(a):
    ls.append(a)


# test1()
test2()
test3()
