import wordcloud
import jieba


def test1():
    # 默认400宽度，200高度
    c = wordcloud.WordCloud(width=600, height=400)
    c.generate('WordCloud for Python')
    c.to_file('wordcloud.png')


def test2():
    txt = "life is short, you need python"
    w = wordcloud.WordCloud(background_color='white')
    w.generate(txt)
    w.to_file("py_wcloud.png")


def test3():
    txt = "程序设计语言是计算机能够理解用户操作意图的一种语言。"
    w = wordcloud.WordCloud(width=1000, font_path='msyh.ttc', height=700)
    w.generate(" ".join(jieba.lcut(txt)))
    w.to_file("py_wcloud.png")


test3()
