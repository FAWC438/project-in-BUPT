import sqlite3

conn=sqlite3.connect('/data/shi.db')
cur=conn.cursor()

file = open("/data/mlzzcf.txt", "r",encoding='UTF-8')
for line in file:  #every line is a poem
    title, author, poem = line.strip().split("::")  #get title and poem
    poem = poem.replace(' ','')
    if len(poem) < 10 or len(poem) > 512:  #filter poem
        continue
    if '_' in poem or '《' in poem or '[' in poem or '(' in poem or '（' in poem:
        continue
    sql="insert into shi values(?,?,?)"
    data=(title,author,poem)
    cur.execute(sql,data)
    conn.commit()
file.close()
conn.close()