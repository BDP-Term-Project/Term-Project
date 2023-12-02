import os
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import pyperclip
import pyautogui
import random

# 옵션 = 출처:전체, 정렬:관련도순, 기간:3개월
# 검색어 = 여행지 추천
# 총 크롤링한 데이터는 60개


user_agent = "user-agent header"
options = Options()
options.add_argument('user-agent=' + user_agent)
options.add_argument('--mute-audio')
options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.implicitly_wait(5)


def move_page(page):
    key_url = 'https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%EC%97%AC%ED%96%89%EC%A7%80+%EC%B6%94%EC%B2%9C&page={}&where=view&nso=so%3Ar%2Cp%3A3m%2Ca%3Aall'.format(
        page)
    return key_url


data = []

for i in range(1, 3):
    url = move_page(i)
    driver.get(url)
    search_url = driver.page_source
    soup = BeautifulSoup(search_url, 'html.parser')
    subj_locate = '.title_area .title_link'
    titles = soup.select(subj_locate)

    for title in titles:
        post_title = title.get_text(strip=True)
        print(post_title)
        data.append(post_title)
    time.sleep(random.uniform(2, 4))

c = os.path.exists('travel_recommendations.txt')
if c:
    os.remove('travel_recommendations.txt')

with open('travel_recommendations.txt', 'w', encoding='utf-8') as f:
    for line in data:
        f.write(line + '\n')