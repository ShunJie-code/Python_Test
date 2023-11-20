fo = open("price2016.csv", "r", encoding='UTF-8')
ls = []
for line in fo:
    line = line.replace("\n", "")
    ls.append(line.split(","))
print(ls)
fo.close()
