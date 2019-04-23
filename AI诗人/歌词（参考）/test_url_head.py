import requests
from bs4 import BeautifulSoup
head={}
head['User-Agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
lrc_url = "http://music.163.com/song?id=30482292"
lyric = requests.get(lrc_url,headers=head)
f=open('test.txt','w',encoding='utf-8')
f.write(lyric.text)
f.close()
