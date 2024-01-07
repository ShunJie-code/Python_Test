import turtle
import datetime


# 根据判断画出单段数码管
def draw_line(draw):
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    turtle.right(90)


# 根据数字绘制一个7段数码管
def draw_digit(d):
    draw_line(True) if d in [2, 3, 4, 5, 6, 8, 9] else draw_line(False)
    draw_line(True) if d in [0, 1, 3, 4, 5, 6, 7, 8, 9] else draw_line(False)
    draw_line(True) if d in [0, 2, 3, 5, 6, 8, 9] else draw_line(False)
    draw_line(True) if d in [0, 2, 6, 8] else draw_line(False)
    turtle.left(90)
    draw_line(True) if d in [0, 4, 5, 6, 8, 9] else draw_line(False)
    draw_line(True) if d in [0, 2, 3, 5, 6, 7, 8, 9] else draw_line(False)
    draw_line(True) if d in [0, 1, 2, 3, 4, 7, 8, 9] else draw_line(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)


# 根据字符串输出一句数码管
def draw_date(date):
    for c in date:
        draw_digit(eval(c))


def main():
    turtle.setup(800, 350, 200, 200)
    turtle.speed("fast")
    turtle.penup()
    turtle.fd(-300)
    turtle.pensize(5)
    date = datetime.datetime.now().strftime('%Y%m%d')
    draw_date(date)
    turtle.hideturtle()


main()
