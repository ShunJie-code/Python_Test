excludes = {'the', 'and', 'of', 'you', 'a', 'i', 'my', 'in'}


def get_text():
    txt = open('hamlet.txt', 'r').read()
    txt = txt.lower()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~':
        txt = txt.replace(ch, " ")
    return txt


hamletTxt = get_text()
words = hamletTxt.split()
# 定义一个字典
counts = {}
for word in words:
    # counts.get(word, 0) word 不存在则返回 0
    counts[word] = counts.get(word, 0) + 1
for word in excludes:
    del(counts[word])

items = list(counts.items())
# 从大到小排序
items.sort(key=lambda x: x[1], reverse=True)
for i in range(10):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count))
