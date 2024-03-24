import jieba
import wordcloud

f = open("新时代中国特色社会主义.txt", "r", encoding="utf-8")
t = f.read()
f.close()
ls = jieba.lcut(t)
txt = " ".join(ls)

# 最新的python换行不再需要\
w = wordcloud.WordCloud(font_path="msyh.ttc", width=1000, height=700,
                        background_color="white")
w.generate(txt)
w.to_file("gr_wordcloud.png")
