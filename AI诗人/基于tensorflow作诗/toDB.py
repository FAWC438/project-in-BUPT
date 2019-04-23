import sqlite3

conn = sqlite3.connect(
    '/dataset/shi.db')
cur = conn.cursor()

file = open("/dataset/poetrySong/poetrySong.txt", "r", encoding='UTF-8')
n = 0
for line in file:  # every line is a poem
    n += 1
    print(n)
    title, author, poem = line.strip().split("::")  # get title and poem
    poem = poem.replace(' ', '')
    if len(poem) < 10 or len(poem) > 512:  # filter poem
        continue
    if '_' in poem or '《' in poem or '[' in poem or '(' in poem or '（' in poem:
        continue
    sql = "insert into shi values(?,?,?)"
    data = (title, author, poem)
    cur.execute(sql, data)
    conn.commit()
file.close()
conn.close()
