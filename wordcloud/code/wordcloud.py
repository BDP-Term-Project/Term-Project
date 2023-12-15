from PIL import Image
import numpy as np
from wordcloud import WordCloud
import matplotlib.pyplot as plt

mapreduce_output_path = '맵리듀스 결과 파일 경로'

with open(mapreduce_output_path, 'r', encoding='utf-8-sig') as f:
    mapreduce_output = f.read()

word_frequencies = {}
for line in mapreduce_output.strip().split('\n'):
    try:
        word, count = line.split()
        word_frequencies[word] = int(count)
    except ValueError:
        print(f"Skipping line: {line}")

img = Image.open('원하는 워드클라우드 이미지 경로')
img_array = np.array(img)
print(img)


if word_frequencies:
    width = 800
    height = 800
    
    wordcloud = WordCloud(width=width, height=height,background_color='white',
                          font_path='Pretendard-Bold',mask=img_array).generate_from_frequencies(word_frequencies)

    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()
else:
    print("No words to generate a word cloud.")