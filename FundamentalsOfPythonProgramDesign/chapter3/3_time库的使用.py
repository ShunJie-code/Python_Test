import time


def test1():
    print(time.time())  # 返回浮点数, 获取当前的时间戳, 从1970 1 1 0:0 开始，到现在的秒数
    print(time.ctime())
    t = time.gmtime()  # 获取计算机可操作的结构体
    print(t.tm_hour, t.tm_min)
    # 时间格式化
    print(time.strftime("%Y-%m-%d %H:%M:%S", t))
    time_str = '2018-01-26 12:50:20'
    t1 = time.strptime(time_str, "%Y-%m-%d %H:%M:%S")
    print(t1.tm_year, t1.tm_mon, t1.tm_mday)
    print(t1.tm_hour, t1.tm_min, t1.tm_sec)


test1()
