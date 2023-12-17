import numpy as np


def test1():
    # 矩阵计算
    # a = np.array([[1, 2, 3], [-3, 4, 5], [6, 7, 8]])
    a = np.array([[1, 2], [-3, 4]])
    print(a)
    #
    print(a.T)
    #
    b = np.linalg.inv(a)
    print(b)
    #
    c = np.linalg.det(a)
    print(c)
    #
    d = np.linalg.matrix_rank(a)
    print(d)
    #
    w, v = np.linalg.eig(a)
    print('eigenvalue=', w)
    print('eigenvector=\n', v)
    #
    x = np.array([3, 2, 1, 1, 1])
    y = np.linalg.norm(x)
    print(y)


test1()
# test2()
