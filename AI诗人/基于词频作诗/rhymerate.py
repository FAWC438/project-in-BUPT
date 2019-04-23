import sqlite3
import re
import pinyin

conn = sqlite3.connect(
    '/data/shi.db')
c = conn.cursor()
print("Opened database successfully")

cursor = c.execute("SELECT title,author,poem  from shi")
rhythmList = ["a", "e", "i", "o", "u"]
sum = 0
isrhtme = 0
for row in cursor:#一个row一首诗
    rhythm = []#储存每句诗的韵脚
    p1 = r"[\u4e00-\u9fa5]{5,7}[\u3002|\uff0c]"  # [汉字]{重复5-7次}[中文句号|中文逗号]
    pattern1 = re.compile(p1)
    result1 = pattern1.findall(row[2])#result把该首诗每句拆分储存
    if result1 == []:
        continue
    for x in result1:
        a = pinyin.get(x[-2], format="strip")
        for y in range(len(a) - 1, -1, -1):
            if a[y] in rhythmList:
                rhythm.append(a[y:])
    temp = list(set(rhythm))  # 设置去除重复项的韵律表

    retD = list(set(rhythm).difference(set(temp)))  # 求差集
    templist = []
    flag = 1
    for i in retD:
        templist.append(rhythm.index(i))
    templist.sort()
    for j in range(len(templist)-1):
        if (templist[j+1]-templist[j]) == 1:
            flag = 0
    
    if len(temp) != len(rhythm) and flag == 1:  # 若有重复且不相邻项说明押韵
        isrhtme += 1
    sum += 1
rate = (isrhtme / sum) * 100
print("The rhyme rate is " + "%.2f" % (rate) + "%")

print("Operation done successfully")
conn.close()