# Okt 사용 고유명사 추출
import csv
from konlpy.tag import Okt

okt = Okt()

csv_file_path = 'naver_api_data/Jeju_naver_api_data.csv'

output_csv_file_path = 'Jeju_okt.csv'

header = ['Extracted tourist attractions']

# 제외 단어 추가
exclude_words = ['여행','여행지','추천','제주','제주도','제주특별자치도','특별자치도']

with open(output_csv_file_path, 'w', encoding='utf-8-sig', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(header)

    with open(csv_file_path, 'r', encoding='utf-8-sig') as csvfile:
        reader = csv.reader(csvfile)

        for row in reader:
            extracted_places = []
            title = row[0]

            nouns = okt.pos(title)
            for noun, pos in nouns:
                if pos == 'Noun' and noun not in exclude_words:
                    extracted_places.append(noun)

            unique_places = list(set(extracted_places))

            print("Extracted tourist attractions:", unique_places)

            writer.writerow([' '.join(unique_places)])
        print("End")