#找出一个歌手的所有专辑，并将里面的所有歌的id存储到csv文件中
import requests
import json
import re
from bs4 import BeautifulSoup
import csv

csv_file=open('test.csv','w',encoding='utf-8',newline='')
writer=csv.writer(csv_file)

url='https://music.163.com/artist/album?id=5347'
head={}
head['User-Agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
web_data = requests.get(url,headers=head)
soup = BeautifulSoup(web_data.text, 'lxml')
rs=list(soup.select('a[class="tit s-fc0"]'))
rex=re.compile(r'"/album\?id=(\d*)">(.*)</a>')

for r in rs:
    mo=rex.search(str(r))
    album_id=mo.group(1)
    album_name=mo.group(2)
    #print(album_id,album_name)

    #找出一张专辑的所有歌的id
    album_url='https://music.163.com/album?id='+album_id
    album_data = requests.get(album_url,headers=head)
    soup_album = BeautifulSoup(album_data.text, 'lxml')
    r_song=str(soup_album.select('ul[class="f-hide"]')[0])
    rex_song=re.compile(r'"/song\?id=(\d*)">(.*?)</a>')
    mo=rex_song.findall(r_song)
    for song_id,song_name in mo:
        print(song_id,song_name)
        writer.writerow([song_id,song_name])

csv_file.close()


