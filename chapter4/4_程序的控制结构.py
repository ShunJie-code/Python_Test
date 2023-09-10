# 异常
def test1():
    try:
        num = eval(input("请输入一个整数: "))
        print(num ** 2)
    # 直接用except 太宽泛，可以指定异常类型
    except NameError:
        print("输入的不是整数")


test1()
