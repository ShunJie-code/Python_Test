"""
os库的使用
路径操作
进程管理
环境参数
"""
import os
import os.path as op
import time


def test1():
    """
    进程管理
    :return:
    """
    os.system("C:\\Windows\\System32\\calc.exe")


def test2():
    """
    环境参数
    :return:
    """
    path = os.getcwd()
    print("Current path is: {}".format(path))
    os.chdir("D:\\")
    path = os.getcwd()
    print("Changed path is: {}".format(path))
    user = os.getlogin()
    cpu_count = os.cpu_count()
    print("Current user is: {}\nCPU count is: {}"
          .format(user, cpu_count))


def test3():
    """
    os.path
    :return:
    """
    # 只能找到当前目录下的绝对路径，即filepath可以正常输出
    filepath = op.abspath("第三方库安装.py")
    filepath1 = op.abspath("test.json")
    # 归一化路径表示形式，将os的其他路径格式统一
    filepath2 = op.normpath("D://codeHUb//ad")
    # 相对路径
    filepath3 = op.relpath("D:\\CodeHub\\Python\\Python_Test\\FundamentalsOfPythonProgramDesign\\chapter7\\test.json")
    # 防止\被认为是转义符号，用\\代替\
    print("D:\\CodeHub\\Python\\Python_Test\\FundamentalsOfPythonProgramDesign\\chapter7\\test.json")
    file_dir = os.path.dirname(filepath)
    file_basename = os.path.basename(filepath)
    print("file_dir = {}".format(file_dir))
    print("file_dir = {}".format(file_basename))
    print(filepath)
    # 注意filepath1 为错误路径
    print(filepath1)  # D:\CodeHub\Python\Python_Test\FundamentalsOfPythonProgramDesign\chapter8\test.json
    print(filepath2)
    print(filepath3)


def test4():
    # True
    print(op.exists("D:\\CodeHub\\Python\\Python_Test\\FundamentalsOfPythonProgramDesign\\chapter7\\test.json"))
    # False
    print(op.exists("D:\\CodeHub\\Python\\Python_Test\\FundamentalsOfPythonProgramDesign\\chapter7\\t.json"))
    # True
    print(op.exists("第三方库安装.py"))
    # False
    print(op.exists("test.json"))
    # True
    print(op.isfile("D:\\CodeHub\\Python\\Python_Test\\FundamentalsOfPythonProgramDesign\\chapter7\\test.json"))
    # False
    print(op.isfile("D:\\CodeHub\\Python\\Python_Test\\FundamentalsOfPythonProgramDesign\\chapter7\\t.json"))
    # True
    print(op.isdir("D:\\CodeHub\\Python\\Python_Test\\FundamentalsOfPythonProgramDesign\\chapter7"))
    # False
    print(op.isdir("D:\\CodeHub\\Python\\Python_Test\\FundamentalsOfPythonProgramDesign\\chapter7\\test.json"))


def test5():
    # 上一次访问的时间
    a = op.getatime("D:\\CodeHub\\Python\\Python_Test\\FundamentalsOfPythonProgramDesign\\chapter7\\test.json")
    time1 = time.ctime(a)

    # 上一次修改的时间
    b = op.getmtime("D:\\CodeHub\\Python\\Python_Test\\FundamentalsOfPythonProgramDesign\\chapter7\\test.json")
    time2 = time.ctime(b)

    # 创建时间
    c = op.getctime("D:\\CodeHub\\Python\\Python_Test\\FundamentalsOfPythonProgramDesign\\chapter7\\test.json")
    time3 = time.ctime(c)
    print("access time = {}\nmodify time = {}\ncreate time = {}".format(time1, time2, time3))


# test2()
test5()
