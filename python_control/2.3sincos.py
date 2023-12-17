import numpy as np
import matplotlib.pyplot as plt


def test1():
    fig, ax = plt.subplots(2, 1)
    x = np.arange(0, 4 * np.pi, 0.1)
    y = np.sin(x)
    z = np.cos(x)
    w = y + z
    # 设置线
    ax[0].plot(x, y, ls='-', label='sin', c='k')
    ax[0].plot(x, z, ls='-.', label='cos', c='b')
    ax[0].set_xlabel('x')
    ax[0].set_ylabel('y, z')
    # 保证前后无余量
    ax[0].set_xlim(0, 4 * np.pi)
    ax[0].grid()
    # 显示图例
    ax[0].legend(loc='upper right')

    ax[1].plot(x, w, color='r', marker='.')
    ax[1].set_xlabel('x')
    ax[1].set_ylabel('w')
    ax[1].set_xlim(0, 4 * np.pi)
    ax[1].grid(ls=':')
    # 防止图形重叠
    fig.tight_layout()
    # 保存为图片
    # fig.savefig("la.png")
    plt.show()


test1()
