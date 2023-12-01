# 현재 크롬버전에 맞는 chromedriver 다운받아놔야 함
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import re

# 크롬 웹드라이버 실행
driver = webdriver.Chrome()
url = 'https://www.instagram.com'
driver.get(url)
time.sleep(3)

# 아이디 입력
email = ''
input_id = driver.find_element(By.CSS_SELECTOR, "#loginForm > div > div:nth-child(1) > div > label > input")
input_id.clear()
input_id.send_keys(email)
# 비번 입력
password = ''
input_pw = driver.find_element(By.CSS_SELECTOR, "#loginForm > div > div:nth-child(2) > div > label > input")
input_pw.clear()
input_pw.send_keys(password)
input_pw.submit()
time.sleep(5)

# 로그인 정보 저장 여부 팝업창 제거 ("나중에 하기 버튼 클릭")
button = driver.find_element(By.CLASS_NAME, "_ac8f")
button.click()
time.sleep(5)

# 알림 설정 팝업창 제거 ("나중에 하기 버튼 클릭")
button2 = driver.find_element(By.CSS_SELECTOR, "body > div.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe > div > div > div._a9-z > button._a9--._ap36._a9_1")
button2.click()
time.sleep(3)

# 해시태그 검색 창에 "여행" 검색
url = "https://www.instagram.com/explore/tags/여행/"
driver.get(url)
time.sleep(10)

# 첫 번째 게시물 클릭
first = driver.find_elements(By.CSS_SELECTOR, "div._aagw")[0]
first.click()
time.sleep(3)

# 게시물에서 본문, 작성일자, 좋아요 수, 위치 정보, 해시태그 가져오는 함수
def get_content(driver):
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    # 본문 내용
    try:
        content = soup.select('h1._ap3a._aaco._aacu._aacx._aad7._aade')[0].text
    except:
        content = ''
    # 해시태그
    tags = re.findall(r'#[^\s#,\\]+', content)
    # 작성일자
    date = soup.select('time._aaqe')[0]['datetime'][:10]
    # 좋아요 수(현재 크롤링 불가능)
    #try:
        #like = soup.select('div._aacl._aaco._aacw._aacx._aada._aade')[0].findAll('span')[-1].text
    #except:
        #like = 0
    # 위치
    try: 
        place = soup.select('div._aaqm')[0].text
    except:
        place = ''
    # data = [content, date, place, tags]
    # 우선 tags랑 place만 저장해놓음
    return [tags, place]

# 다음 게시물로 클릭 이동시키는 함수
def move_next(driver):
    next = driver.find_element(By.CSS_SELECTOR, "div._aaqg._aaqh")
    next.click()
    time.sleep(3)

# 결과 저정할 리스트
results = []
# 수집할 게시물 수
target = 10
for i in range(target):
    try:
        data = get_content(driver)
        results.append(data)
        print(i+1)
        move_next(driver)
    except:
        time.sleep(2)
        move_next(driver)
    time.sleep(1)

# 결과 출력
# print(results)

result_df = pd.DataFrame(results)
result_df.columns = ['tags', 'place']
# encoding = utf-8-sig로 해야 한글 안 깨짐
result_df.to_csv('insta_travel_crawling.csv', index=False, encoding='utf-8-sig')
