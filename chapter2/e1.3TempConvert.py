# -*- coding:utf-8 -*-
"""
作者：xsj
日期：2023年 08月 13日
"""


def temp_convert(value_str):
    if value_str[-1] in ['f', 'F']:
        c = (eval(value_str[0: -1]) - 32) / 1.8
        print("转换后的温度是{:.2f}C".format(c))
    elif value_str[-1] in ['c', 'C']:
        f = 1.8 * eval(value_str[0: -1]) + 32
        print("转换后的温度是{:.2f}F".format(f))
    else:
        print("输入的格式有误")


temp_str = input("请输入带有符号的温度值：")
temp_convert(temp_str)


def test1():
    for i in range(5):
        print("Hello", i)
    for i in range(2, 5):
        print("world", i)


test1()
