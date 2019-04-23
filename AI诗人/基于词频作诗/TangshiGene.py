import random
import time
import pinyin


def search(array, target):
    # array为二维数组
    for index in range(len(array)):
        if target in array[index]:
            return True
    return False


# 生成五言律诗
def Line5():
    noun = open('/data/freqword_n.txt',
                encoding='utf-8').readlines()
    verb = open('/data/freqword_v.txt',
                encoding='utf-8').readlines()

    nounlist = []
    for word in noun:
        i = 0
        while i < len(word):
            if word[i:i + 2] != "\n" and word[i] != ' ' and word[i + 1] != ' ':
                nounlist.append(word[i:i + 2])
            i = i + 3

    verblist = []
    for word in verb:
        i = 0
        while i < len(word):
            if word[i:i + 2] != "\n" and word[i] != ' ' and word[i + 1] != ' ':
                verblist.append(word[i:i + 2])
            i = i + 3

    num = 0

    rhythm = ""
    rhythmList = [['a', 'ua', 'ia'], ['e', 'o', 'uo'], ['e', 'ie', 've'], ['i', 'v', 'er'], ['u'], ['ai', 'uai'], ['ei', 'ui'], ['ao', 'iao'], [
        'ou', 'iu'], ['an', 'ian', 'uan', 'van'], ['en', 'in', 'un', 'vn'], ['ang', 'iang', 'uang'], ['eng', 'ing', 'ueng', 'ong', 'iong']]  # 汉字十三辙
    while num < 4:  # 诗句数量可调整为8句绝句
        i = random.randint(1, len(nounlist) - 1)
        i1 = random.randint(1, len(nounlist) - 1)
        j = random.randint(1, len(verblist) - 1)

        ind = 0
        ind1 = 0
        if num == 0:

            #首句用绝句的仄起仄收式：仄仄平平仄
            a = [[0],[0]]
            b = [5]
            c = [[5],[0]]
            while int(a[0][-1])<3 or int(a[1][-1])<3 or int(b[-1])>2 or int(c[0][-1])>2 or int(c[1][-1])<3:
                i = random.randint(1, len(nounlist) - 1)
                i1 = random.randint(1, len(nounlist) - 1)
                j = random.randint(1, len(verblist) - 1)
                a = pinyin.get(nounlist[i], delimiter=" ", format="numerical").split()
                b = pinyin.get(verblist[j][1], delimiter=" ", format="numerical")
                c = pinyin.get(nounlist[i1], delimiter=" ", format="numerical").split()
                
            #以下是押韵的处理
            rhythm = ""
            verse = pinyin.get(nounlist[i1][1], format="strip")
            for p in range(len(verse)):
                if search(rhythmList, verse[p:]):
                    ind = p
            rhythm = verse[ind:]

        if num != 0:
            ind1 = 0
            verse1 = pinyin.get(nounlist[i1][1], format="strip")
            for p in range(len(verse1)):
                if search(rhythmList, verse1[p:]):
                    ind1 = p

            while verse1[ind1:] != rhythm:
                i1 = random.randint(1, len(nounlist) - 1)
                verse1 = pinyin.get(nounlist[i1][1], format="strip")
                for p in range(len(verse1)):
                    if search(rhythmList, verse1[p:]):
                        ind1 = p

        print(nounlist[i] + verblist[j][1] + nounlist[i1])      #可通过修改此处变为律诗
        num += 1


if __name__ == '__main__':
    Line5()
