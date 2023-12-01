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

