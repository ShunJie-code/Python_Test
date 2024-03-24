"""
JSON格式
1 数据保存在键值对中
2 键值对之间用逗号分割
3 大括号用于保存键值对数据组成的对象
4 方括号用于保存键值对数据组成的数组
"""
import json


def test1():
    dt = {'b': 2, 'c': 4, 'a': 6}
    # dumps 字典转化为字符串；按照json格式编码,不排序也不缩进对其
    s1 = json.dumps(dt)
    print(s1, type(s1))

    s2 = json.dumps(dt, sort_keys=True, indent=4)  # 设置排序和缩进
    print('{}\ns1==s2? {}'.format(s2, 'True' if s1 == s2 else 'False'))

    # loads 字符串转化为字典，将json格式字符串转换为python的数据类型
    dt2 = json.loads(s2)
    print(dt2, type(dt2))

    # 使用dump和load写入和读出json文件
    fp = open('test.json', 'w')
    json.dump(dt, fp, sort_keys=True, indent=4)
    fp.close()

    fp = open('test.json', 'r')
    dt3 = json.load(fp)
    fp.close()

    print('dt3 = {}'.format(dt3))


test1()
