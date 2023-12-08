# 형태소 분석: twitter

from wordcloud import WordCloud
import matplotlib.pyplot as plt

mapreduce_output_path = '지역_mapreduce_result.txt 경로'  # Replace with the correct path

with open(mapreduce_output_path, 'r', encoding='utf-8-sig') as f:
    mapreduce_output = f.read()
print(mapreduce_output)

word_frequencies = {}
for line in mapreduce_output.strip().split('\n'):
    try:
        word, count = line.split()
        word_frequencies[word] = int(count)
    except ValueError:
        print(f"Skipping line: {line}")

print("Word Frequencies:", word_frequencies)

# Generate and display the word cloud with adjusted aspect ratio
if word_frequencies:
    width = 800
    height = 800
    
    wordcloud = WordCloud(width=width, height=height, background_color='Black',colormap="Pastel2",font_path='/Windows/Fonts/NanumSquareB.ttf').generate_from_frequencies(word_frequencies)

    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()
else:
    print("No words to generate a word cloud.")
