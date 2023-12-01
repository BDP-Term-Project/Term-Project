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
