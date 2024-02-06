import json

"""
python字典常用方法：
　　　　keys()              #  获取所有的键
　　　　values()            #  获取所有的值
　　　　items()             #  获取所有的键值对，成对的对象
　　　　get()               #   获取某个键的值
　　　　update()            #   用来更新字典
　　　　pop()               #   用来删除某个键值对
"""
fr = open("price2016.json", "r", encoding="utf-8")
ls = json.load(fr)

data = [list(ls[0].keys())]
for item in ls:
    data.append(list(item.values()))
fr.close()
fw = open("price2016_from_json.csv", "w", encoding="utf-8")
for item in data:
    fw.write(",".join(item) + "\n")
fw.close()
