# -*- coding:utf-8 -*-
"""
作者：xsj
日期：2023年 07月 31日
"""
import sys

from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    # 传入运行程序时的参数列表
    app = QApplication(sys.argv)

    w = QWidget()

    w.setWindowTitle("第一个pyqt程序")

    w.show()

    app.exec()
