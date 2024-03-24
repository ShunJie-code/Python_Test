import json


def test1():
    dt = {'b': 2, 'c': 4, 'a': 6}
    s2 = json.dumps(dt, sort_keys=True, indent=6)
    print(s2)


def test2():
    textfile = open("7.1.txt", "rt", encoding='utf-8')
    # 读1行
    print(textfile.readline())
    textfile.close()

    b_text = open('7.1.txt', 'rb')
    print(b_text.readline())
    b_text.close()


def test3():
    # 解析中文需要带编码格式参数
    fo = open('7.1.txt', 'w+', encoding='utf-8')
    # 读所有行
    ls = ['唐诗', '宋词', '元曲']

    fo.writelines(ls)
    fo.seek(0)
    for line in fo:
        print(line)
    fo.close()


def test4():
    ls = ['中国', '美国', '英国']
    # 文件的join写入与split读出
    fp = open('7.1.txt', 'w', encoding='utf-8')
    fp.write('$'.join(ls))
    fp.close()
    fp = open('7.1.txt', 'r', encoding='utf-8')
    ls2 = fp.read().split('$')
    print(ls2)


# test2()
# test3()
test4()
