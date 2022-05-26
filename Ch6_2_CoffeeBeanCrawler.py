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
    
    element = wd.find_element_by_id('localTitle')
    element.click()
    time.sleep(1)
    
    element = wd.find_element(By.XPATH, '//*[@id="storeLocal"]/li[2]/a')
    element.click()
    time.sleep(1)

    element = wd.find_element_by_id('localTitle2')
    element.click()
    time.sleep(1)
    
    element = wd.find_element(By.XPATH, '//*[@id="storeLocal2"]/li[9]/a')
    element.click()
    time.sleep(1)
    
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
