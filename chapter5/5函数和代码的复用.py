"""
函数
"""


def fact(n):
    s = 1
    for i in range(1, n + 1):
        s *= i
    return s


def fact_divided(n, m=1):
    # 可选参数传递
    s = 1
    for i in range(1, n + 1):
        s *= i
    # 双斜杠表示整除
    return s // m


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


test1()
