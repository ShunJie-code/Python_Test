""" 天天向上与工作日努力的对比 """


def day_day_up1(factor):
    day_up = 1.0
    for i in range(365):
        if i % 7 in [6, 0]:
            day_up *= (1 - 0.01)
        else:
            day_up *= (1 + factor)
    return day_up


df = 0.01
while day_day_up1(df) < 37.78:
    df += 0.001
print("与天天向上一样的工作日努力的参数是: {:.3f}".format(df))
