"""
收尾双下划线方法为特殊方法
"""

a = 10
b = 20

print(dir(a))   # python 中一切皆对象,可查看有方法

print('-'*40)
print("{}, {}, {}".format(a + b, a.__add__(b), a.__sub__(b)))
print('-'*40)
print(a.__pow__(2))
