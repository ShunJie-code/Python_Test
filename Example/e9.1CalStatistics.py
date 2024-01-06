from math import sqrt


def get_num():
    nums = []
    num_str = input('请输入数字(回车退出): ')
    while num_str != '':
        nums.append(eval(num_str))
        num_str = input('请输入数字(回车退出): ')
    return nums


def mean(numbers):
    s = 0.0
    for num in numbers:
        s += num
    return s / len(numbers)


def dev(numbers, m):
    s = 0.0
    for num in numbers:
        s += (num - m) ** 2
    return sqrt(s / (len(numbers) - 1))


def median(numbers):
    new = sorted(numbers)
    size = len(numbers)
    if size % 2 == 0:
        med = (new[size // 2 - 1] + new[size // 2]) / 2
    else:
        med = new[size // 2]
    return med


def main():
    numbers = get_num()
    m = mean(numbers)
    print("平均值：{:.2} 标准差：{:.2} 中位数：{}".format(m, dev(numbers, m),
                                                       median(numbers)))


main()
