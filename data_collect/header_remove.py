import pandas as pd
import os

# 여러 지역들의 파일 목록
regions = ['Busan', 'Chungbuk', 'Daegu', 'Gyeongbuk', 'Gyeongnam', 'Incheon', 'Jeju', 'Seoul', 'Chungnam', 'Daejeon', 'Gangwon', 'Gwangju', 'Jeonbuk', 'Jeonnam' ,'Gyeonggi', 'Sejong', 'Ulsan']  # 다른 지역들도 리스트에 추가

# 각 지역 파일들의 첫 번째 행 삭제
for region in regions:
    file_path = f'BDP_Project/insta_crawling_csv/{region}_insta_data.csv'

    if os.path.exists(file_path):  # 파일이 존재하는지 확인
        # CSV 파일 불러오기 (첫 번째 행은 제외하고 읽기)
        df = pd.read_csv(file_path, skiprows=[0])

        # 수정된 데이터프레임을 파일로 저장 (기존 파일을 덮어쓰게 됨)
        df.to_csv(file_path, index=False, encoding='utf-8-sig')

        print(f"First row removed from {region}_insta_data.csv file.")
    else:
        print(f"{region}_insta_data.csv file not found.")