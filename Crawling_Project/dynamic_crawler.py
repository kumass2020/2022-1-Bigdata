from selenium import webdriver
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
import time
from bs4 import BeautifulSoup

def returnDriver(self):
    options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    options.add_argument('window-size=960x1000')
    options.add_argument('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36')
    options.add_argument("lang=en_US")
    options.add_argument("timezone=UTC+9")

    driver = webdriver.Chrome('chromedriver', chrome_options=options)
    driver.execute_script("Object.defineProperty(navigator, 'languages', {get: function() {return ['en_US', 'en']}})")

    return driver

def crawl(result):
    driver = returnDriver()
    wait = WebDriverWait(driver, 10)

    url = 'https://twitter.com/elonmusk'
    driver.get(url)

    # 페이지 로딩까지 대기
    wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, 'article')))

    # 페이지 바닥까지 내려서 컨텐츠 로딩 시키기
    # 현재 스크롤 높이
    last_height = driver.execute_script("return document.body.scrollHeight")

    # 바닥까지 반복
    while True:
        # 스크롤 다운
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # 로딩 대기
        time.sleep(1)

        new_height = driver.execute_script("return document.body.scrollHeight")
        # 더 이상 스크롤 되지 않으면 while문 escape
        if new_height == last_height:
            break
        last_height = new_height

    # driver의 현재 page source로 beautifulsoup 객체 생성
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    tweet = soup.select('.css-901oao.r-1nao33i.r-37j5jr.r-a023e6.r-16dba41.r-rjixqe.r-bcqeeo.r-bnwqim.r-qvutc0')
    
    # 파싱할 tweet의 갯수
    print(len(tweet))


if __name__=="__main__":
    crawl()