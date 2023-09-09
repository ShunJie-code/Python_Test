""" 基本数据类型 """
import math


# 整数有四种类型
def test1():
    x = 0b010 + 0b011
    print(x)


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


day_up = math.pow((1.0 + 0.001), 365)
day_down = math.pow((1 - 0.001), 365)

print("向上：{}")
