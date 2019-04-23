import sqlite3
import re
import pinyin

conn = sqlite3.connect(
    'C:/Users/qq185/OneDrive - bupt.edu.cn/python/AI璇椾汉-2018211604-2018213344-鍑屽浗鐎�/鍩轰簬tensorflow浣滆瘲/dataset/shi.db')
c = conn.cursor()
print("Opened database successfully")

cursor = c.execute("SELECT title,author,poem  from shi")
for row in cursor:
    rhythm = []
    p1 = r"[\u4e00-\u9fa5]{5,7}[\u3002|\uff0c]"  # [姹夊瓧]{閲嶅5-7娆[涓枃鍙ュ彿|涓枃閫楀彿]
    pattern1 = re.compile(p1)
    result1 = pattern1.findall(row[2])
    if result1 == []:
        continue
    for x in result1:
        a = pinyin.get(x[-2], format="strip")
        for y in range(len(a) - 1, -1, -1):
            if a[y] in rhythmList:# 这个list看你想压哪种韵了
                rhythm.append(a[y:])
    temp = list(set(rhythm))
    if len(temp) != len(rhythm):
        isrhtme += 1
    sum += 1
rate = (isrhtme / sum) * 100
print("The rhyme rate is " + "%.2f" % (rate) + "%")

print("Operation done successfully")
conn.close()
