"""
字符串-元组-列表 都是序列类型
"""


# 总共有6个操作符
def test1():
    ls = ['python', 123, '.io']
    ls1 = ls[::-1]
    print(ls1)
    s = 'python123'
    s1 = s[::-1]
    print(s1)
    print(len(s))
    print(min(s))
    print(max(s))
    print(s.index('p'))
    print(s + s1)


def func():
    # 多元返回值就是元组类型
    return 1, 2


def test2():
    a = func()
    print(a)
    print(type(a))
    # 直接用逗号分割的变量也是元组类型
    creature = 'cat', 'dog', 'tiger'
    print(creature, type(creature))
    # 元组嵌套
    color = (0x111000, 'blue', creature)
    print(color, type(color))
    # 基本继承了序列类型所有的操作
    creature1 = creature[::-1]
    print(creature1)
    print(color[-1][2])


#     列表
def test3():
    # 内存中创建了列表
    ls = [1, 2]
    # 内存中并没有创建列表
    lt = ls
    ls += lt
    del ls[2]
    print(ls)
    ll = ['cat', 'dog', 'tiger', 1024]
    # 相当与拿掉一个，增加两个
    ll[1:2] = [1, 2, 3]
    print(ll)
    # 相当于增加一个子列
    ll[1] = [1, 3]
    print(ll)


# test1()
# test2()
test3()