"""
os库的使用
路径操作
进程管理
环境参数
"""
import os
import os.path as op


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
    # filepath = op.abspath("第三方库安装.py")
    filepath1 = op.abspath("test.json")

    # 归一化路径表示形式，将os的其他路径格式统一
    filepath2 = op.normpath("D://codeHUb//ad")
    # 相对路径
    filepath3 = op.relpath(filepath1)

    # file_dir = os.path.dirname(filepath)
    # file_basename = os.path.basename(filepath)
    # print("file_dir = {}".format(file_dir))
    # print("file_dir = {}".format(file_basename))
    # print(filepath)
    print(filepath1)

    print(filepath2)
    print(filepath3)


# test2()
test3()
