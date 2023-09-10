""" 向上5天与向下2天 """


def day_day_up(factor):
    day_up = 1.0
    for i in range(365):
        if i % 7 in [6, 0]:
            day_up *= (1 - factor)
        else:
            day_up *= (1 + factor)
    print("向上5天向下2天的力量: {:.2f}".format(day_up))


day_day_up(0.01)
