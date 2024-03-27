"""
映射 key -> value
"""


def test1():
    d = {"中国": "北京", "美国": "华盛顿", "法国": "巴黎"}
    print(d)
    d['英国'] = '伦敦'
    if '中国' in d:
        print('yes')
    print(d.keys())
    print(d.values())
    print(d['法国'])
    print(d.get('中国', '伊斯兰堡'))
    print(d.get('巴基斯坦', '伊斯兰堡'))
    print(d.popitem())
    print(len(d))


def test2():
    d = {'a': 1, 'b': 2}
    print("d['b'] = {}".format(d['b']))
    d['b'] = 7
    for k in d:
        print(d[k])
    if 'c' in d:
        print('yes')
    d.clear()
    print(len(d))


test1()
# test2()
