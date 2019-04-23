import requests
from bs4 import BeautifulSoup
lrc_url = "http://music.163.com/song?id=30482292"
lyric = requests.get(lrc_url)
f=open('test.txt','w',encoding='utf-8')
f.write(lyric.text)
f.close()
