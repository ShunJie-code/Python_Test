"""
门特卡罗方法计算pi, 概率统计法，计算思维
"""
from random import random
from time import perf_counter


def test0():
    for k in range(1, 10 + 1):
        print(k)  # 1---10


def test1():
    darts = 1000 * 1000 * 2
    # 提高后续除法精度
    hits = 0.0
    start = perf_counter()
    for i in range(1, darts + 1):
        x, y = random(), random()
        dist = pow(x ** 2 + y ** 2, 0.5)
        if dist <= 1.0:
            hits += 1
    pi = 4 * (hits / darts)
    dur = perf_counter() - start
    print("圆周率的值是:{}".format(pi))
    print("运行的时间是：{}".format(dur))


# test0()
test1()
