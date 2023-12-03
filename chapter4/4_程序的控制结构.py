# 异常 try except else finally 高级用法
def test1():
    try:
        # num = eval(input("请输入一个整数: "))
        num = input("请输入一个整数: ")
        print(int(num) ** 2)
    # 直接用except 太宽泛，可以指定异常类型 # except:
    except ValueError:
        print("输入的不是整数")
    else:
        print("输入是整数")
    finally:
        print("程序已退出")


def test3():
    try:
        num = eval(input("请输入一个整数: "))
        print(num ** 2)
    except NameError:
        print("输入的不是整数")


# 紧凑结构 只能用表达式
def test2():
    guess = eval(input())
    print("猜{}了".format("对" if guess == 99 else "错"))


test1()
# test2()
