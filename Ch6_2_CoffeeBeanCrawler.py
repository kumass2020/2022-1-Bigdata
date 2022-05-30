from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#[CODE 1]
def CoffeeBean_store(result):
    CoffeeBean_URL = "https://www.coffeebeankorea.com/store/store.asp"
    wd = webdriver.Chrome('./chromedriver.exe')
             
    wd.get(CoffeeBean_URL)
    time.sleep(1)
    
    element = wd.find_element_by_id('region_srh')
    element.click()
    time.sleep(1)
    
    element = wd.find_element(By.ID, 'localTitle')
    element.click()
    time.sleep(1)
    
    # 경기 선택
    element = wd.find_element(By.XPATH, '//*[@id="storeLocal"]/li[2]/a')
    element.click()
    time.sleep(1)

    element = wd.find_element(By.ID, 'localTitle2')
    element.click()
    time.sleep(1)
    
    # 성남시 분당구 선택
    element = wd.find_element(By.XPATH, '//*[@id="storeLocal2"]/li[9]/a')
    element.click()
    time.sleep(1)

    ############################################################################
    
    # 서울 찾기 시작
    # dropdown menu를 펼침
    element = wd.find_element(By.ID, 'localTitle')
    element.click()
    time.sleep(1)
    
    element = wd.find_element(By.ID, 'storeLocal')
    elements = element.find_elements(By.TAG_NAME, 'li')     # 지역명이 나와있는 리스트들을 찾고
    for element in elements:        
        if element.text == '경기':  # 텍스트에 경기를 갖고 있는 요소를 찾아냅니다.
            break
    
    element.find_element(By.TAG_NAME, 'a')  # 해당 요소 하위 태그인 a 태그를 찾아내 클릭
    element.click()
    
    time.sleep(1)
    
    # 성남시 분당구 찾기 시작 (위와 동일한 방식입니다.)
    # dropdown menu를 펼침
    element = wd.find_element_by_id('localTitle2')
    element.click()
    time.sleep(1)
    
    element = wd.find_element(By.ID, 'storeLocal2')
    elements = element.find_elements(By.TAG_NAME, 'li')
    for element in elements:
        if element.text == '성남시 분당구':
            break
    
    element.find_element(By.TAG_NAME, 'a')
    element.click()
    
    
    return

#[CODE 0]
def main():
    result = []
    print('CoffeeBean store crawling >>>>>>>>>>>>>>>>>>>>>>>>>>')
    CoffeeBean_store(result)  #[CODE 1]
    
    CB_tbl = pd.DataFrame(result, columns=('store', 'address','phone'))
    CB_tbl.to_csv('.CoffeeBean.csv', encoding='cp949', mode='w', index=True)

if __name__ == '__main__':
     main()
