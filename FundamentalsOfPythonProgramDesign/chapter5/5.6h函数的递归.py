"""
递归的两个关键特征
链条+基例
函数+分支
不断开辟内存执行
"""


def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


def rvs(s):
    if s == '':
        return s
    else:
        return rvs(s[1:]) + s[0]


def f(n):
    if n == 1 or n == 2:
        return 1
    else:
        return f(n - 1) + f(n - 2)


count = 0


def hanoi(n, src, dst, mid):
    global count
    if n == 1:
        print("{}: {} -> {}".format(1, src, dst))
        count += 1
    else:
        hanoi(n - 1, src, mid, dst)
        print("{}: {} -> {}".format(n, src, dst))
        count += 1
        hanoi(n - 1, mid, dst, src)


print(fact(5))
# 字符串反转 s[::-1]
s = 'abcd'
print(rvs(s))
print(f(1), f(2), f(3), f(4), f(5))

hanoi(3, 'a', 'c', 'b')
print(count)
