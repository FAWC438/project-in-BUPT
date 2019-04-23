# coding: utf-8
import jieba.analyse
from os import path
from scipy.misc import imread
import matplotlib as mpl
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

if __name__ == "__main__":

    mpl.rcParams['font.sans-serif'] = ['FangSong']
    #mpl.rcParams['axes.unicode_minus'] = False

    file = open("/dataset/poetrySong/onlypoem.txt", "rb").read()

    # tags extraction based on TF-IDF algorithm
    tags = jieba.analyse.extract_tags(file, topK=100, withWeight=False)
    text = " ".join(tags)
    # read the mask
    d = path.dirname(__file__)
    trump_coloring = imread(path.join(d, "dataset\\Trump.png"))

    wc = WordCloud(font_path='/data/simsun.ttc',# date文件夹在词频作诗中
                   background_color="black", max_words=3000, mask=trump_coloring,
                   max_font_size=200, random_state=42)

    # generate word cloud
    wc.generate(text)

    # generate color from image
    image_colors = ImageColorGenerator(trump_coloring)

    plt.imshow(wc)
    plt.axis("off")
    plt.show()
