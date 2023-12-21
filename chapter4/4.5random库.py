import random


def test1():
    # 不给种子的时候，种子是当前时间
    # 种子可以使随机数复现
    random.seed(10)
    r = random.random()
    s = random.random()
    t = random.random()
    print(r, s, t)  # 0.5714 0.428889


def test2():
    # random.seed(1)
    i = random.randint(10, 100)
    j = random.choice(range(100))
    k = random.uniform(0, 10)
    print("{}, {}, {}".format(i, j, k))


test1()
# test2()
