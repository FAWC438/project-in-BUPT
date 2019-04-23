import re

poemfile = open('/dataset/poetrySong/poetrySong.txt', encoding='UTF-8').read()

p1 = r"[\u4e00-\u9fa5]{5,7}[\u3002|\uff0c]"
pattern1 = re.compile(p1)
result1 = pattern1.findall(poemfile)

with open('/dataset/poetrySong/onlypoem.txt', 'w+', encoding='utf-8') as f:  # 打开输出文件
    for x in result1:
        f.write(x)
