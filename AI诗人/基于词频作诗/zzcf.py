import re

poemfile = open('/data/poem.txt', encoding='UTF-8').read()
new_poemfile = open('/dataset/poetryTang/poetryTang.txt', encoding='UTF-8').read() # 在机器学习文件夹里

p1 = r"[\u4e00-\u9fa5]{5,7}[\u3002|\uff0c]"     #[汉字]{重复5-7次}[中文句号|中文逗号]

pattern1 = re.compile(p1)        #题目和作者
result1 = pattern1.findall(poemfile) 
result2 = pattern1.findall(new_poemfile)   #搜索匹配的字符串，得到匹配列表

with open('/data/zzcf.txt','w+',encoding='utf-8') as f: #打开输出文件
    for x in result1:
        f.write(x)
    for y in result2:
        f.write(y)