import json


fr = open("price2016.csv", "r", encoding='utf-8')
# ls 存放二维数据
ls = []
for line in fr:
    line = line.replace("\n", "")
    ls.append(line.split(','))
print(ls)
fr.close()
fw = open("price2016.json", "w", encoding='utf-8')
for i in range(1, len(ls)):
    ls[i] = dict(zip(ls[0], ls[i]))
print(ls)
"""
[['城市', '环比', '同比', '定基'], {'城市': '北京', '环比': '101.5', '同比': '120.7', '定基': '121.4'}, 
{'城市': '上海', '环比': '101.2', '同比': '127.3', '定基': '127.8'}, {'城市': '广州', '环比': '101.3', '同比': '119.4', '定基': '120.0'}, 
{'城市': '深圳', '环比': '102.0', '同比': '140.9', '定基': '145.5'}, {'城市': '沈阳', '环比': '100.1', '同比': '101.4', '定基': '101.6'}]
"""
# 直接dump，中文会输出成unicode编码，排序也按此进行
# json.dump(ls[1:], fw, indent=4, sort_keys=True)
json.dump(ls[1:], fw, indent=4, ensure_ascii=False)
fw.close()
