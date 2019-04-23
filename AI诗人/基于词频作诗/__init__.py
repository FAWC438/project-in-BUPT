import urllib3
from bs4 import BeautifulSoup
import certifi
import time
import random
import re

rex=re.compile(r'\(.*?\)')

f = open('/data/s_song.txt', "w+",encoding="utf-8")
http = urllib3.PoolManager(
    cert_reqs='CERT_REQUIRED',
    ca_certs=certifi.where())

for poemId in range(1, 1001):
    print(poemId)
    url ='https://www.gushiwen.org/shiwen/default_3A888888888888A'+str(poemId)+'.aspx'
    #'http://www.gushiwen.org/wen_' + str(poemId) + '.aspx' 原始
    #content = soup.find('div', class_="contson").get_text()
    #file.write(content)

    #'https://www.gushiwen.org/shiwen/default.aspx?page=' + str(poemId) 所有诗
    #'https://www.gushiwen.org/shiwen/default_3A666666666666A'+str(poemId)+'.aspx'   唐诗
    #'https://www.gushiwen.org/shiwen/default_3A888888888888A'+str(poemId)+'.aspx'   宋诗
    r = http.request('GET', url)
    soup = BeautifulSoup(r.data, 'html.parser')
    content = soup.find('div', class_="contson").get_text()
    content = re.sub(rex, "", content)
    content = content.replace('\n', '')
    author = soup.find('p', class_="source").get_text()
    author.replace('\n', '')
    author=author[author.find("：")+1:]
    title = soup.find('b').get_text()
    title.replace('\n', '')
    result=(title+'::'+author+'::'+content+'\n')
    # if poemId >= 1109 and poemId < 2010:
    #     file.write(content)
    f.write(result)
    time.sleep(random.random()*3)
f.close()