import time
# clock不能用，改用perf_counter
t1 = time.perf_counter()
# sleep中的时间单位为s
time.sleep(0.1)
time.sleep(1.2)
t2 = time.perf_counter()
t = t2 - t1
print("{:.2f}s".format(t))  # 1.32s
