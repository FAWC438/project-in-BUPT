#测试通过163api住区一首歌的歌词，并用JSON模块解析
import requests
import json
lrc_url = 'http://music.163.com/api/song/lyric?id=30482292&lv=1&kv=1&tv=-1'
lyric = requests.get(lrc_url)
j = json.loads(lyric.text)
print(j['lrc']['lyric'])
