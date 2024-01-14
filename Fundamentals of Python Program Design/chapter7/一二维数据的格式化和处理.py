# m7.8GetCSV2List
def test1():
    fo = open("price2016.csv", "r", encoding='UTF-8')
    ls = []
    for line in fo:
        line = line.replace("\n", "")
        ls.append(line.split(","))
    print(ls)
    fo.close()


# m7.9GetCSVbyLine
def test2():
    fo = open("price2016.csv", "r", encoding='utf-8')
    for line in fo:
        line = line.replace('\n', '')
        ls = line.split(",")
        lns = ""
        for s in ls:
            lns += "{}\t".format(s)
        print(lns)
    fo.close()


# 7.10WriteD1toCSV
def test3():
    fo = open("price2016bj.csv", "w")  # 写文件，没有该文件则创建
    ls = ['北京', '101.5', '120.7', '121.4']
    fo.write(",".join(ls) + "\n")
    fo.close()


# 7.11WriteD2toCSV
def test4():
    fr = open("price2016.csv", 'r', encoding="utf-8")
    fw = open("price2016out.csv", 'w')
    ls = []
    for line in fr:
        line = line.replace('\n', '')
        ls.append(line.split(','))
    for i in range(len(ls)):
        for j in range(len(ls[i])):
            if ls[i][j].replace(".", "").isnumeric():
                ls[i][j] = "{:.2}%".format(float(ls[i][j]) / 100)
    for row in ls:
        print(row)
        fw.write(",".join(row) + "\n")
    fr.close()
    fw.close()


# test1()
test4()
