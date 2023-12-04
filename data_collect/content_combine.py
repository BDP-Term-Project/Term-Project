# extracted_tags 컬럼 삭제, content 내용 뒤에 place추가해서 열 하나로 합치기
import pandas as pd

# CSV 파일 경로
csv_file_path = '울산_extract_hashtag.csv'
# CSV 파일 읽기
df = pd.read_csv(csv_file_path)

# 'extracted_tags' 열 삭제
df = df.drop('extracted_tags', axis=1)

# 'content' 열 끝에 ','로 'place' 열의 내용 추가
df['content'] = df.apply(lambda row: row['content'] + ', ' + row['place'] if pd.notnull(row['place']) else row['content'], axis=1)

# 'place' 열 삭제
df = df.drop('place', axis=1)

# 결과를 새로운 CSV 파일로 저장
output_csv_file_path = 'ulsan_insta_data.csv'
df.to_csv(output_csv_file_path, encoding='utf-8-sig', index=False)
