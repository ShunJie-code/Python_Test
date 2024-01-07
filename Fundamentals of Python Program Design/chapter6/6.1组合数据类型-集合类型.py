"""
集合
"""


def test1():
    a = {'p', 'y', 123}
    # 集合特点1 不按照定义的顺序打印
    print(a)  # y 123 p
    b = set('pypy123')
    print(b)  # 相当不重复出现的5个字符
    c = a - b
    print(c)
    c = b - a  # 求差
    print(c)
    c = a & b  # 求交集
    print(c)
    c = a | b  # 求并集
    print(c)
    c = a ^ b  # 求补集
    print(c)


def test2():
    a = {"p", "y", 123}
    print(a)
    for item in a:
        print(item, end='')
    try:
        while True:
            print(a.pop(), end='')
    except KeyError:
        pass


def test3():
    # 数据去重
    ls = ['p', 'p', 'y', 'y', 123]
    s = set(ls)
    lt = list(s)
    print(lt)


# test1()
# test2()
test3()
