import numpy as np
import matplotlib.pyplot as plt


def test1():
    x = np.arange(0, 4 * np.pi, 0.1)
    y = np.sin(x)
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.show()


def test2():
    x = np.arange(0, 4 * np.pi, 0.1)
    y = np.sin(x)
    # 使用面向对象的方法
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.grid()
    plt.show()


test1()
test2()
