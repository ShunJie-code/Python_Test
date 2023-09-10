""" 基本数据类型 """
import math


# 整数有四种类型，2、8、10、16进制
def test1():
    x = 0b010 + 0b011
    y = 0xa + 0xb
    z = 0o10 + 0o3
    print(x, y, z)


# 浮点数运算存在不确定位数0.1 + 0.2
def test2():
    if 0.1 + 0.2 == 0.3:
        print("yes")
    # 取小数第一位
    if round(0.1 + 0.2, 1) == 0.3:
        print("True")
    # 浮点数的科学计数法
    a = 4.3e-3 + 10E2
    print(a)


# 复数类型
def test3():
    z = 10 + 6j
    print(z.real)
    print(z.imag)


def test4():
    x = 10
    y = 3
    print(x / y, x // y, x * y, x ** y)
    print(x % y)
    pi = 3.1416
    # 二元操作符
    pi **= 3
    print(pi)


# python 数值运算函数
def test5():
    print(abs(-10.2))
    # 同时输出商和余数
    x, y = divmod(10, 3)
    print(x, y)
    # 幂运算后取余，最后一个参数，可有可无
    print(pow(3, 3, 10))
    # 最大最小
    print(max(1, 10, 5))
    print(min(1, 10, 5))
    # int 和 float函数
    print(int("123"), float("12.34"))
    print(int(123.45), float(12))
    x = complex(x)
    print(x)


# DayDayUp 数学思维 to 计算程序思维
def day_day_up(factor):
    day_up = pow((1 + factor), 365)
    day_down = pow((1 - factor), 365)
    print("向上: {:.2f}, 向下: {:.2f}".format(day_up, day_down))


def day_day_up1(factor):
    day_up = 1.0
    for i in range(365):
        if i % 7 in [6, 0]:
            day_up *= (1 - 0.01)
        else:
            day_up *= (1 + factor)
    print("工作日的力量: {:.2f}".format(day_up))
    return day_up


# test1()
# test2()
# test3()
# test4()
# test5()
day_day_up(0.001)
day_day_up(0.005)
day_day_up(0.01)
day_day_up1(0.01)
df = 0.01
while day_day_up1(df) < 37.78:
    df += 0.001
print(df)
