import pandas as pd
import glob

# 여러 CSV 파일을 읽어서 DataFrame으로 합치기
folder_path = './naver_crawling_data/gyeonggi/'
csv_files = glob.glob(f'{folder_path}/*.csv')
df_list = [pd.read_csv(file, header=None) for file in csv_files]
concatenated_df = pd.concat(df_list, ignore_index=True)

# 새로운 CSV 파일로 저장
output_file_path = './naver_crawling_data/concate_gyeonggi.csv'
concatenated_df.to_csv(output_file_path, header=False, index=False, encoding='utf-8-sig')