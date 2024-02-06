import json


fr = open("price2016.csv", "r", encoding='utf-8')
# ls 存放二维数据
ls = []
for line in fr:
    line = line.replace("\n", "")
    ls.append(line.split(','))
fr.close()
fw = open("price2016.json", "w", encoding='utf-8')
for i in range(1, len(ls)):
    ls[i] = dict(zip(ls[0], ls[i]))
# 直接dump，中文会输出成unicode编码，排序也按此进行
# json.dump(ls[1:], fw, indent=4, sort_keys=True)
json.dump(ls[1:], fw, indent=4, ensure_ascii=False)
fw.close()
