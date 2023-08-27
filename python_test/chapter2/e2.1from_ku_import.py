# -*- coding:utf-8 -*-
"""
作者：xsj
日期：2023年 08月 27日
"""
from turtle import *
Screen().setup(650, 500, 200, 200)

# 抬起画笔
penup()
# 海归前动为fd
fd(-250)
pendown()
pensize(25)
pencolor("purple")
# 改变海龟的角度
seth(-40)
for i in range(4):
    # 以海归当前位置左侧某一点为圆心 (r, angle)
    circle(40, 80)
    circle(-40, 80)
circle(40, 80/2)
fd(40)
circle(16, 180)
fd(40 * 2/3)
# 可以阻塞画图操作
done()
