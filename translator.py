import requests
import json
from bs4 import BeautifulSoup as bs

print('欢迎使用'.center(104, '*')+'\n')
print('粗制滥造的翻译'.center(101, '*')+'\n')
print('Designed by Kevin Ling'.center(108, '*')+'\n')
print("按回车可退出哦".center(101, '-')+'\n')
word = input("请输入中文或英文：")
while word != '':
    f = 'zh-CHS'
    t = 'en'
    for i in word:
        if '\u4e00' <= i <= '\u9fff':
            break
    else:
        f = 'en'
        t = 'zh-CHS'
    data = {
        'from': f,
        'text': word,
        'to': t}
    header = {
        'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763'
    }

    s = requests.Session()
    r = s.post(
        'https://cn.bing.com/ttranslate?&category=&IG=539FCEEC9B5549D599780B3F02D0F1D7&IID=translator.5037.16', data=data,
        headers=header)
    result = json.loads(r.content.decode())
    print("翻译结果是：" + result['translationResponse'])
    word = input("请输入中文或英文：")
