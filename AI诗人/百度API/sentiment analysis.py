import re
import numpy as np
from aip import AipNlp
import random
import time

APP_ID = '15397946'
API_KEY = ''
SECRET_KEY = ''

client = AipNlp(APP_ID, API_KEY, SECRET_KEY)  # 登录百度云

poemfile = open('/data/zzcf.txt', encoding='UTF-8').read()# 词频作诗
p1 = r"[\u4e00-\u9fa5]{5,7}[\u3002|\uff0c]"
pattern1 = re.compile(p1)
result1 = pattern1.findall(poemfile)

list_positive = []
list_negative = []
list_confidence = []
list_sentiment = []

i = 0
j = 0
print('第'+str(j)+'秒')
for row in result1:  # 每句诗的情感分析     注意：百度要求request限制为5个/秒
    try:
        i += 1
        temp = client.sentimentClassify(row)
        list_positive.append(temp['items'][0]['positive_prob'])
        list_negative.append(temp['items'][0]['negative_prob'])
        list_confidence.append(temp['items'][0]['confidence'])
        list_sentiment.append(temp['items'][0]['sentiment'])
        if i == 5:
            j += 1
            print('第'+str(j)+'秒')
            i = 0
            time.sleep(1)
    except:
        break


# 乐观
avg_positive = np.mean(list_positive)  # 平均数，下同

# 悲观
avg_negative = np.mean(list_negative)

# 可信度
avg_confidence = np.mean(list_confidence)

# 乐悲观总体评价
counts = np.bincount(list_sentiment)
rate_positive = counts[2] / sum(counts)
rate_neutral = counts[1] / sum(counts)
rate_negative = counts[0] / sum(counts)
s = ""
if np.argmax(counts) == 0:  # 众数
    s = "悲观"
elif np.argmax(counts) == 1:
    s = "中性"
else:
    s = "乐观"


print("在整首诗的数据库中，诗句乐观倾向约为{:.2f}%，诗句悲观倾向约为{:.2f}%，数据总体可信度为{:.2f}%。".format(
    avg_positive * 100, avg_negative * 100, avg_confidence * 100))
print("乐观诗句占比约为{:.2f}%,中性诗句占比约为{:.2f}%，悲观诗句占比约为{:.2f}%，以{}诗为最多。".format(
    rate_positive*100, rate_neutral*100, rate_negative*100, s))
