import requests
import re
from bs4 import BeautifulSoup

import time
import random

import sqlite3

conn=sqlite3.connect('/shi.db')
cur=conn.cursor()


f=open('shi.txt','w',encoding='utf-8')

rex=re.compile(r'\(.*?\)')

for i in range(1,3000):
    print('Spidering Page:'+str(i)+'...')

    url = 'https://www.gushiwen.org/shiwen/default.aspx?page=' + str(i)
    #'https://www.gushiwen.org/shiwen/default_3A666666666666A'+str(i)+'.aspx'   唐诗
    #'https://www.gushiwen.org/shiwen/default_3A666666666666A'+str(i)+'.aspx'   宋诗
    web_data = requests.get(url)

    soup = BeautifulSoup(web_data.text, 'lxml')
    contents=soup.select('div[class="left"]')[1]
    contents=list(contents.select('div[class="sons"]'))

    

    for c in contents:
        title=c.select('b')[0].text
        title.replace('\n','')
        author=c.select('p[class="source"]')[0].text
        author.replace('\n', '')
        author=author[author.find("：")+1:]         #去除朝代
        text=c.select('div[class="contson"]')[0].text
        text=re.sub(rex,"",text)
        text=text.replace('\n','')
        f.write(title+'::'+author+'::'+text+'\n')

        sql="insert into shi values(?,?,?)"
        data=(title,author,text)
        cur.execute(sql,data)
        conn.commit()

    #每抓一页一定要休息几秒，否则会被网站封ip
    time.sleep(random.random()*3)

f.close()
conn.close()
