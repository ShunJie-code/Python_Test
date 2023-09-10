""" 天天向上的力量 """


def day_day_up(factor):
    day_up = pow((1 + factor), 365)
    day_down = pow((1 - factor), 365)
    print("{}: 向上 {:.2f}, 向下 {:.2f}".format(factor, day_up, day_down))


day_day_up(0.001)
day_day_up(0.005)
day_day_up(0.01)
