"""
1 定义数据文件格式
300,0,144,1,0,0
行进距离，转向判断，转向角度，RGB三通道颜色
2 编程
3 编制数据文件

自动化思维：
    数据和功能分离，数据驱动的自动运行
接口化设计：
    格式化设计接口，清晰明了
二维数据应用：
    应用维度组织数据，二维数据最常用
"""
import turtle as t
t.title('自动轨迹绘制')
t.setup(800, 600, 0, 0)
t.pencolor('red')
t.pensize(5)

data_ls = []
f = open('data.txt')
for line in f:
    line = line.replace('\n', '')
    # line.split 分割
    # map函数，将第一个参数的功能作用于第二个参数的每一个元素
    # list函数, 子列表
    data_ls.append(list(map(eval, line.split(','))))
f.close()

for i in range(len(data_ls)):
    t.pencolor(data_ls[i][3], data_ls[i][4], data_ls[i][5])
    t.fd(data_ls[i][0])
    if data_ls[i][1]:
        t.right(data_ls[i][2])
    else:
        t.left(data_ls[i][2])
