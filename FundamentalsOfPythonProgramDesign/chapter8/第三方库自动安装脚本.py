"""
BatchInstall
"""
import os

libs = ['numpy', 'matplotlib', 'sympy', 'pandas', 'wheel']
try:
    for lib in libs:
        os.system("pip install " + lib + " -i https://pypi.tuna.tsinghua.edu.cn/simple")
    print("successful")
except:
    print("Failed somehow")
