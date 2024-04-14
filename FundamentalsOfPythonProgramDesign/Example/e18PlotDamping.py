"""
实例18 阻尼衰减曲线坐标图绘制
"""
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
"""
科学坐标图的4个要素：
坐标轴、数据曲线、标题、图注
"""
matplotlib.rcParams['font.family'] = 'SimHei'
matplotlib.rcParams['font.sans-serif'] = ['SimHei']


def draw(x, y, z, pcolor, nt_point, nt_text, nt_size):
    """
    :param x:
    :param y:
    :param z:
    :param pcolor:
    :param nt_point:
    :param nt_text:
    :param nt_size:
    :return: 绘制曲线
    """
    plt.plot(x, y, color=pcolor, label="$exp_{decay}$",
             linewidth=3, linestyle="-")
    plt.plot(x, z, 'b--', label="$cos(x^2)$", linewidth=1)
    plt.xlabel('时间(s)')
    plt.ylabel('幅度(mV)')
    plt.title("阻尼衰减曲线绘制")
    plt.annotate(r"$\cos(2 \pi t) \exp(-t)$",
                 xy=nt_point,
                 xytext=nt_text,
                 fontsize=nt_size,
                 arrowprops=dict(arrowstyle='->', connectionstyle="arc3,rad=0.2"))


def xy_axis(x_start, x_end, y_start, y_end):
    """
    :param x_start:
    :param x_end:
    :param y_start:
    :param y_end:
    :return: 修改坐标轴
    """
    plt.xlim(x_start, x_end)
    plt.ylim(y_start, y_end)
    plt.xticks([np.pi/3, 2*np.pi/3, np.pi, 4*np.pi/3, 5*np.pi/3],
               [r'$\pi/3$', r"$2\pi/3$", r"$\pi$", r"$4\pi/3$", r"$5\pi/3$"])


def test():
    x = np.linspace(0, 6.0, 100)

    # 先把两条曲线的表达式写出
    y = np.cos(2*np.pi*x) * np.exp(-x) + 0.8
    z = 0.5 * np.cos(x ** 2) + 0.8
    note_point = (1, np.cos(2 * np.pi) * np.exp(-1) + 0.8)
    note_text = (1, 1.4)
    note_size = 14
    plt.figure(figsize=(8, 6), facecolor='white')
    plt.subplot(111)
    draw(x, y, z, 'red', note_point, note_text, note_size)

    # 设置坐标系的范围
    ix = (x > 0.8) & (x < 3)
    plt.text(0.5*(0.8+3), 0.2, r"$\int_a^b f(x)\mathrm{d}x$",
             horizontalalignment='center')
    plt.fill_between(x, y, 0, where=ix, facecolor='grey', alpha=0.25)

    xy_axis(0, 5, 0, 1.8)

    plt.legend()

    plt.savefig('sample.JPG')

    plt.show()


test()
