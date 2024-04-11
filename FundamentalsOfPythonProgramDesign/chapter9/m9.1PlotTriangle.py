import numpy as np

import matplotlib.pyplot as plt

x = np.linspace(0, 6, 100)
y = np.cos(2 * np.pi * x) * np.exp(-x) + 0.8
# 第三个参数代表曲线的颜色 'k' == 黑色；也可以用color='r'赋值
plt.plot(x, y, 'k', linewidth=3, linestyle='-')
plt.show()
