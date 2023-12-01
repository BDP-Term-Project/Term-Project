import os
import sys
import urllib.request
import csv
import json


client_id = "FVG3wWlAd0pWsd2o4gf2"
client_secret = "6wh5CKV19L"
encText = urllib.parse.quote("여행지")

csv_file_path = "naver_api_data.csv"

#sort = 정확도순으로 검색
#display = 보여주는 개수
#네이버 api에서 검색 제공하는 기능중에 start라는 파라미터가 존재함. 이는 범위가 1~1000까지 정해져있는데 기본적으로 1로 되어있어 for 문을 통해 1000까지 돌림
#display가 100개 이므로 범위1~10으로 해서 *100한다음에 url에 값에 넘긴다.


for i in range(1, 11):
    start_num = i * 100
    print("시작 위치:"+start_num)
    url = "https://openapi.naver.com/v1/search/blog?query=" + encText + "&display=100&sort=sim&start=" + str(start_num) # JSON 결과
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
            
   
            csv_writer.writerow(['Title'])
            
           #검색하는 단어에 <b>,</b>태그가 붙어있기 떄문에 이를 뺴줌
            for item in data['items']:
                for item in data['items']:
                    title_without_tags = item['title'].replace('<b>', '').replace('</b>', '')
                    csv_writer.writerow([title_without_tags])
    else:
        print("Error Code:" + rescode)