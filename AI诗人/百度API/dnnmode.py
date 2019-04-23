import re
import numpy as np
from aip import AipNlp
import random
import time

APP_ID = '15397946'
API_KEY = ''# 密码
SECRET_KEY = ''# ……另一个密码

client = AipNlp(APP_ID, API_KEY, SECRET_KEY)  # 登录百度云

poemfile = open('/data/zzcf.txt', encoding='UTF-8').read()# 在词频作诗中
p1 = r"[\u4e00-\u9fa5]{5,7}[\u3002|\uff0c]"
pattern1 = re.compile(p1)
result1 = pattern1.findall(poemfile)

list_ppl = []

i = 0
j = 0
print('第'+str(j)+'秒')
for row in result1:  # 每句诗的情感分析     注意：百度要求request限制为5个/秒
    try:
        i += 1
        temp = client.dnnlm(row)
        list_ppl.append(temp['ppl'])
        if i == 5:
            j += 1
            print('第'+str(j)+'秒')
            i = 0
            time.sleep(1)
    except:
        break

avg_ppl = np.mean(list_ppl)

print("该诗词数据的可读性平均得分为{:.2f}。（该分值越小表示可读性越好）".format(avg_ppl))
