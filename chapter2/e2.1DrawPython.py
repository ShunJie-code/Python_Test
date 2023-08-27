# PythonDraw.py
import turtle

# 长度高度，起始点的坐标
turtle.setup(650, 500, 200, 200)


def python_draw():
    # 抬起画笔
    turtle.penup()
    # 海归前动为fd
    turtle.fd(-250)
    turtle.pendown()
    # 画笔的宽度
    turtle.pensize(25)
    # 也可以用rgb指令
    # turtle.pencolor(0.63, 0.13, 0.94)
    turtle.pencolor("purple")
    # 改变海龟的角度
    turtle.seth(-40)
    for i in range(4):
        # 以海归当前位置左侧某一点为圆心 (r, angle)
        turtle.circle(40, 80)
        turtle.circle(-40, 80)
    # 方向摆正
    turtle.circle(40, 80/2)
    turtle.fd(40)
    turtle.circle(16, 180)
    turtle.fd(40 * 2/3)
    # 可以阻塞画图操作
    # turtle.done()


def test1():
    # 绝对坐标
    turtle.goto(100, 100)
    turtle.goto(100, -100)
    turtle.goto(-100, -100)
    turtle.goto(-100, 100)
    turtle.goto(0, 0)
    turtle.done()


def test2():
    # 海归坐标
    turtle.left(45)
    turtle.fd(150)
    turtle.right(135)
    turtle.fd(300)
    turtle.left(135)
    turtle.fd(150)
    turtle.done()


def test3():
    # 绘制圆形
    turtle.circle(100)


python_draw()
# turtle.clear()
# test1()
# test2()
# test3()
