#从test.csv中读取所有歌曲id及歌名，每一首歌以歌名为文件名建立一个文本文件，并将歌词写入其中
import requests
import json
import re

savepath='lrc/'
import csv
csv_file=open('test.csv','r',encoding='utf-8')
reader=list(csv.reader(csv_file))
for [song_id,song_name] in reader:
    lrc_url = 'http://music.163.com/api/song/lyric?' + 'id=' + song_id + '&lv=1&kv=1&tv=-1'
    lyric = requests.get(lrc_url)
    json_obj = lyric.text
    j = json.loads(json_obj)
    #使用try块，避免这首歌没有提供歌词
    try:
        lrc = j['lrc']['lyric']
        pat = re.compile(r'\[.*\]')
        lrc = re.sub(pat, "", lrc)
        lrc = lrc.strip()
        f=open(savepath+song_name+'.txt','w',encoding='utf-8')
        f.write(lrc)
        f.close()
    except KeyError as e:
        pass
