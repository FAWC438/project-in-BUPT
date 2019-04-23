#读取歌词文件，整理成Chinese_poem的格式
import os
path='lrc/'
songs=os.listdir(path)
data=[]
for song in songs:
    f = open(path+song,encoding='utf-8')
    txt=f.read()
    lrc=[]
    #用回车分开，以行为单位进行处理
    for row in txt.split('\n'):
        #如果某一行包含：或者:
        #说明这是歌曲信息，不是歌词正文，予以丢弃
        if '：' not in row and ':' not in row :
            row=row.strip()
            #去掉空格后检查文本长度，避免空文本
            if len(row)>0:
                #两句歌词如果是空格隔开，则将空格改为逗号
                row='，'.join(row.split())+'。'
                lrc.append(row)
    #通过检查文件名（不包含.txt）来获得歌名
    song=song.split('.')[0]
    #整理成Chinese_poem的格式
    data.append(song+'::'+'汪峰'+'::'+''.join(lrc))
    
f=open('wangfeng.txt','w',encoding='utf-8')
#最后将所有的文本用\n连起来写入txt文件中
f.write('\n'.join(data))
f.close()
        
