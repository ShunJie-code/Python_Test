"""
os库的使用
"""
import os


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


test2()
