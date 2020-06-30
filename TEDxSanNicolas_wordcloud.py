import matplotlib.pyplot as plt
from os import path
from wordcloud import WordCloud
from nltk.corpus import stopwords

stop_words_sp=set(stopwords.words('spanish'))

def random_color_func_incierto(word=None, font_size=None, position=None, orientation=None, font_path=None, random_state=None):
    h = int(100.0 * 895.0 / 255.0)
    s = int(100.0 * 214.0 / 255.0)
    l = int(100.0 * float(random_state.randint(16, 150)) / 255.0)

    return "hsl({}, {}%, {}%)".format(h, s, l)

def random_color_func_cierto(word=None, font_size=None, position=None, orientation=None, font_path=None, random_state=None):
    h = int(100.0 * 170.85 / 255.0)
    s = int(100.0 * 175.95 / 255.0)
    l = int(100.0 * float(random_state.randint(16, 150)) / 255.0)

    return "hsl({}, {}%, {}%)".format(h, s, l)

file_content_raw_incierto=open ("docs/incertezas.txt", encoding="utf8").read()

file_content_raw_cierto=open ("docs/certezas.txt", encoding="utf8").read()

wordcloud_incierto = WordCloud(font_path = r'C:\Windows\Fonts\Verdana.ttf',
                            stopwords = stop_words_sp,                            
                            background_color = "white",
							max_words= 70,
                            width = 2000,
                            height = 3000,
							color_func = random_color_func_incierto
                            ).generate(file_content_raw_incierto)

plt.imshow(wordcloud_incierto)
plt.axis('off')
plt.show()

wordcloud_cierto = WordCloud(font_path = r'C:\Windows\Fonts\Verdana.ttf',
                            stopwords=stop_words_sp,
                            background_color = 'white',
							max_words= 70,
                            width = 2000,
                            height = 3000,
							color_func = random_color_func_cierto
                            ).generate(file_content_raw_cierto)

plt.imshow(wordcloud_cierto)
plt.axis('off')
plt.show()