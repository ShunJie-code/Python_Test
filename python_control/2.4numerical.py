from scipy.integrate import odeint  # 积分模块
import sympy as sp  # 因式分解求根
import numpy as np
import matplotlib.pyplot as plt


def system(y, t):
    if t < 10.0:
        u = 0.0
    else:
        u = 1.0
    dydt = (-y + u) / 5
    return dydt


def test1():
    y0 = 0.5
    t = np.arange(0, 100, 0.04)
    # 函数+初值+自变量，即可求微分方程的解
    y = odeint(system, y0, t)
    fig, ax = plt.subplots()
    ax.plot(t, y, label='y')
    ax.plot(t, 1 * (t >= 10), ls='--', label='u')
    ax.set_xlabel('t')
    ax.set_ylabel('y, u')
    ax.legend(loc='best')
    ax.grid(ls=':')
    plt.show()


def test2():
    sp.init_printing()
    s = sp.Symbol('s')
    f = 2*s**2 + 5*s + 3
    root = sp.solve(f, s)
    print(root)
    g = sp.factor(f, s)
    print(g)
    h = sp.expand(g, s)
    print(h)


# test1()
test2()
