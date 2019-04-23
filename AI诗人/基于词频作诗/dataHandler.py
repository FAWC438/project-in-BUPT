import time
import jieba
import jieba.analyse

poetry_file = '/data/zzcf.txt'
n_file = '/data/freqword_n.txt'
v_file = '/data/freqword_v.txt'
a_file = '/data/freqword_a.txt'
ag_file = '/data/freqword_ag.txt'

content = open(poetry_file, encoding='utf-8').read()

t1 = time.time()

count = 0
with open(n_file, 'w+', encoding='utf-8') as f1:
    for x in jieba.analyse.textrank(
            content, topK=600, allowPOS=('n', 'nr', 'ns', 'nt', 'nz', 'm')):
        f1.writelines(x + " ")
        count += 1
        if count % 10 == 0:
            f1.write("\n")

count = 0
with open(v_file, 'w+', encoding='utf-8') as f2:
    for x in jieba.analyse.textrank(content, topK=400, allowPOS=('v', 'vg')):
        f2.writelines(x + " ")
        count += 1
        if count % 10 == 0:
            f2.write("\n")

count = 0
with open(a_file, 'w+', encoding='utf-8') as f3:
    for x in jieba.analyse.textrank(
            content, topK=400, allowPOS=('a', 'ad', 'an')):
        f3.writelines(x + " ")
        count += 1
        if count % 10 == 0:
            f3.write("\n")

count = 0
with open(ag_file, 'w+', encoding='utf-8') as f4:
    for x in jieba.analyse.textrank(content, topK=400, allowPOS=('ag')):
        f4.writelines(x + " ")
        count += 1
        if count % 10 == 0:
            f4.write("\n")

t2 = time.time()
tm_cost = t2 - t1

print("time cost: " + str(tm_cost) + "秒")
