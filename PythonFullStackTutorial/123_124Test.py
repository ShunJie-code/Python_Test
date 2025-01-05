"""
123 选择题
124 计算圆的面积和周长

"""


class Circle:
    def __init__(self, r):
        self.r = r

    def get_area(self):
        return 3.14 * pow(self.r, 2)

    def get_perimeter(self):
        return 2 * 3.14 * self.r


def test():
    r = eval(input('请输入圆的半径：'))
    c = Circle(r)

    area = c.get_area()
    perimeter = c.get_perimeter()
    print(area, perimeter)


if __name__ == '__main__':
    test()
