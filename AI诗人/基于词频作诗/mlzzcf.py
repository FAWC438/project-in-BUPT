import re

poemfile = open('/data/poem.txt',encoding='UTF-8').read()



p1 = r"([\u300c]\S*[\u300d])([\u4e00-\u9fa5]{1,25})"    #题目 作者
p2 = r"([\u5377])(\S*)"     #卷……
p3 = r"([\u2014])(\S*)"    #——
p4 = r"([\uff1b])(\S*)([\uff1b])"     #处理后的整首诗
p5 = r"([\uff08])(\S*)([\uff08])"#（）
p6 = r"([\u300c](\S*)[\u300d])"#题目格式
pattern1 = re.compile(p1)        #题目和作者
result1 = pattern1.findall(poemfile)   #搜索匹配的字符串，得到匹配列表
poemfile = re.sub(p2,'',poemfile)
poemfile = re.sub(p3,'',poemfile)
poemfile = re.sub(p1,'；；',poemfile)
poemfile = re.sub(p5,'',poemfile)
poemfile = re.sub(p6,'',poemfile)
poemfile = ''.join(poemfile.split())
pattern2 = re.compile(p4)
result2 = pattern2.findall(poemfile)#诗句
s = result2[0][1]
s = s[1:-2]
l = s.split("；；")
i = 0

with open('/data/mlzzcf.txt','w+',encoding='utf-8') as f: #打开mlzzcf
    for x in result1:
        if i != len(l) - 1:
            i+=1
        else:
            break
        f.write(x[0][1:-1] + "::" + x[1] + "::" + l[i] + '\n')
'''
with open('D:/data/Chinese_poem_generator-master/dataset/poetryTang','a+',encoding='utf-8') as f1: #加入机器学习的源数据中
    for x in result1:
        if i != len(l) - 1:
            i+=1
        else:
            break
        f1.write(x[0][1:-1] + "::" + x[1] + "::" + l[i] + "\n")
'''