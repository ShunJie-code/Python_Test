class A:
    pass


class B:
    pass


class C(A, B):
    def __init__(self, name, age):
        self.name = name
        self.age = age


a = A()
b = B()
c = C('xaj', 20)

print("对象a的属性字典:", a.__dict__)
print("对象b的属性字典:", b.__dict__)
print("对象c的属性字典:", c.__dict__)

print("对象a的所属的类:", a.__class__)
print("对象b的属性字典:", b.__class__)
print("对象c的属性字典:", c.__class__)

print("A的父类:", A.__bases__)
print("B的父类:", B.__bases__)
print("C的父类:", C.__bases__)
print("C的父类:", C.__base__)  # 输出第一个父类

print("A层次结构:", A.__mro__)
print("B层次结构:", B.__mro__)
print("C层次结构:", C.__mro__)


print("A的子类列表:", A.__subclasses__())
print("B的子类列表:", B.__subclasses__())
print("C的子类列表:", C.__subclasses__())
