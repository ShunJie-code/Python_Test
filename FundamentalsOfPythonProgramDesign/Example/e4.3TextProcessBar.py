import time


def test1():
    # clock不能用，改用perf_counter
    t1 = time.perf_counter()
    # sleep中的时间单位为s
    time.sleep(0.1)
    time.sleep(1.2)
    t2 = time.perf_counter()
    t = t2 - t1
    print("{:.2f}s".format(t))  # 1.32s


def test2():
    scale = 50
    # // 为结果向下舍入到最接近的整数
    print("执行开始".center(scale // 2, '-'))
    # t = time.perf_counter()
    t0 = time.time()
    for i in range(scale + 1):
        a = "*" * i
        b = '.' * (scale - i)
        c = (i / scale) * 100
        # t -= time.perf_counter()
        t = time.time() - t0
        print("\r{:^3.0f}% [{}->{}]{:.2f}s".format(c, a, b, t), end='')
        time.sleep(0.05)
    print("\n" + "执行结束".center(scale // 2, '-'))


def test3():
    # clock不能用，改用perf_counter
    t = time.time()
    for i in range(3):
        # sleep中的时间单位为s
        time.sleep(0.1)
        a = 3 * 3
        time.sleep(2.2)
        b = a
        t1 = time.time()
        t2 = t1 - t
        print("{:.2f}s".format(t2))  # 1.32s


test2()
# test3()
# time.clock() # 该方法不能用
