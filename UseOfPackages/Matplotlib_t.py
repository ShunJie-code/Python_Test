import matplotlib.pyplot as plt
import numpy as np
from pylab import mpl
# 设置显示中文字体
mpl.rcParams["font.sans-serif"] = ["SimHei"] # 黑体
# 设置正常符号显示
mpl.rcParams["axes.unicode_minus"] = False
# %matplotlib widget 日期设置为简洁格式
mpl.rcParams['date.converter'] = 'concise'


print(plt.style.available) # 样式显示
import matplotlib.pyplot as plt
plt.figure(figsize=(12, 6), dpi=80)
plt.subplot(251)
plt.bar([1,2,3],[1,2,3])
plt.style.use('Solarize_Light2')
plt.subplot(252)
plt.bar([1,2,3],[1,2,3])
plt.style.use('_classic_test_patch')
plt.subplot(253)
plt.bar([1,2,3],[1,2,3])
plt.style.use(['fivethirtyeight'])
plt.subplot(254)
plt.bar([1,2,3],[1,2,3])
plt.style.use(['ggplot'])
plt.subplot(256)
plt.bar([1,2,3],[1,2,3])
# plt.style.use('seaborn-bright')
plt.subplot(257)
plt.bar([1,2,3],[1,2,3])
plt.show()