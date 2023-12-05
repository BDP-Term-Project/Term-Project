import os
import sys
import urllib.request
import csv
import json


client_id = "client키"
client_secret = "client비밀번호"




#sort = 정확도순으로 검색
#display = 보여주는 개수
#네이버 api에서 검색 제공하는 기능중에 start라는 파라미터가 존재함. 이는 범위가 1~1000까지 정해져있는데 기본적으로 1로 되어있어 for 문을 통해 1000까지 돌림
#display가 100개 이므로 범위1~10으로 해서 *100한다음에 url에 값에 넘긴다.

sigun_list_kor = ["서울특별시", "부산광역시","대구광역시","인천광역시","광주광역시","대전광역시","울산광역시","세종특별자치도","경기도",
                  "강원특별자치도","충청북도","충청남도","전라북도","전라남도","경상북도","경상남도","제주특별자치도"]
sigun_list_en = ["Seoul","Busan","Daegu","Incheon","Gwangju", "Daejeon","Ulsan","Sejong","Gyeonggi",
                 "Gangwon", "Chungbuk","Chungnam","Jeonbuk", "Jeonnam","Gyeongbuk","Gyeongnam","Jeju"]


for j in range(len(sigun_list_kor)):
    
    print(sigun_list_kor[j] + ':' + sigun_list_en[j])

    encText = urllib.parse.quote(sigun_list_kor[j] + "여행지")

    csv_file_path = sigun_list_en[j]+"_naver_api_data.csv"

    for i in range(0,10):
        start_num = i*100 + 1
        url = "https://openapi.naver.com/v1/search/blog?query=" + encText + "&sort=sim&display=100&start=" + str(start_num) # JSON 결과
        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id",client_id)
        request.add_header("X-Naver-Client-Secret",client_secret)
        response = urllib.request.urlopen(request)
        rescode = response.getcode()

        if(rescode==200):
            response_body = response.read()
            data = json.loads(response_body)


            #csv가 미리있다면 append를 통해 기존 파일에 적어줌
            with open(csv_file_path, 'a', newline='', encoding='utf-8-sig') as csv_file:
                csv_writer = csv.writer(csv_file)
                
            #검색하는 단어에 <b>,</b>태그가 붙어있기 떄문에 이를 뺴줌
                for item in data['items']:
                    title_without_tags = item['title'].replace('<b>', '').replace('</b>', '')
                    csv_writer.writerow([title_without_tags])
        else:
            print("Error Code:" + rescode)
