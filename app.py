from wordcloud import WordCloud
import os

import matplotlib.pyplot as plt

with open('words.txt', 'r') as file:
    data = file.read().replace('\n', '')

cloud = WordCloud(background_color="white").generate(data)
plt.imshow(cloud)
plt.axis("off")
figure = plt.gcf()

figure.set_size_inches(16, 4)
plt.savefig(os.environ['FILENAME'], dpi=100)
