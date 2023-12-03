import pandas as pd
import re

# insta_travel_crawling_도시 형태로 저장된 csv에서 tags의 해쉬태그 #뒤에 붙은 string만 추출해서 extracted_tags에 저장
dosi = ['강원', '경기', '광주', '대전', '세종', '울산', '전북', '충남']

# CSV 파일 불러오기
for d in dosi:
    file_path = f'insta_travel_crawling_{d}.csv'
    df = pd.read_csv(file_path)

    # 각 문자열에서 #뒤에 있는 단어들 추출하는 함수
    def extract_tags(tags_list):
        # 결과를 저장할 빈 리스트
        extracted_tags = []
        
        # 각 문자열에서 #뒤에 있는 단어들 추출
        for tags_str in tags_list:
            tags = re.findall(r'#([^\s#,\\]+)', tags_str)
            extracted_tags.extend(tags)
        
        return extracted_tags

    # 'tags' 컬럼에 대해 extract_tags 함수를 적용하여 'extracted_tags' 컬럼 추가
    df['extracted_tags'] = df['tags'].apply(eval).apply(extract_tags)


    # 필요한 컬럼만 남기기
    selected_columns = ['content', 'extracted_tags', 'place']
    # 새로운 DataFrame 생성
    new_df = df[selected_columns]
    # 새로운 CSV 파일로 저장
    new_file_path = f'{d}_extract_hashtag.csv'
    new_df.to_csv(new_file_path, index=False, encoding='utf-8-sig')

