# 字符串共有两类四种表示方法
# 由一对单引号或双引号表示，仅表示单行字符串
# “请输入带有符号的温度值” ‘C’
# 由一对三单引号或三双引号表示，可表示多行字符串，文件头说明实质是字符串
"""
python
语言
"""


def test1():
    print('这里有"号')
    print('''这里有'又有"''')


def test2():
    # [M:N:K] 允许缺失
    print("012345"[:3])
    # [M:N:K] 根据步长K对字符切片
    print("0123456789"[1:8:2])
    # 字符串逆序
    print("0123456789"[::-1])


def test3():
    test_string = "1 + 1 = 2 " + chr(10004)
    print(test_string)


# 打印 12 星座序列
def test4():
    for i in range(12):
        print(chr(9800 + i), end="")  # end=“” 表示输出不换行

# 字符串类型的格式化-槽


# test1()
# test2()
# test3()
test4()

