from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
import time
from bs4 import BeautifulSoup
import pandas as pd

def returnDriver():
    options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    options.add_argument('window-size=960x1000')
    options.add_argument('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36')
    options.add_argument("lang=en_US")
    options.add_argument("timezone=UTC+9")

    driver = webdriver.Chrome('./Crawling_Project/chromedriver', chrome_options=options)
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

    current_y = 1080
    while True:
        # current_y = driver.execute_script("return document.body.scrollHeight")
        # driver.execute_script("window.scrollTo(0, " + str(int(current_y) - 1080) +");")
        
        new_y = current_y + 1080
        
        driver.execute_script("window.scrollTo(0, " + str(new_y) +");")

        # driver의 현재 page source로 beautifulsoup 객체 생성
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        # tweets = soup.select('.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1ny4l3l')
        tweets = soup.select('.css-1dbjc4n.r-1iusvr4.r-16y2uox.r-1777fci.r-kzbkwu')
        
        # 파싱할 tweet의 갯수
        print(len(tweets))

        for tweet in tweets:
            tweet_writer_span = tweet.select('.css-901oao.css-16my406.css-bfa6kz.r-poiln3.r-bcqeeo.r-qvutc0')[0]
            tweet_id_div = tweet.select('.css-901oao.css-bfa6kz.r-1bwzh9t.r-18u37iz.r-37j5jr.r-a023e6.r-16dba41.r-rjixqe.r-bcqeeo.r-qvutc0')[0]
            tweet_datetime_a = tweet.select('.css-4rbku5.css-18t94o4.css-901oao.r-1bwzh9t.r-1loqt21.r-1q142lx.r-37j5jr.r-a023e6.r-16dba41.r-rjixqe.r-bcqeeo.r-3s2u2q.r-qvutc0')[0]
            tweet_text_div = tweet.select('.css-901oao.r-1nao33i.r-37j5jr.r-a023e6.r-16dba41.r-rjixqe.r-bcqeeo.r-bnwqim.r-qvutc0')
            # 인용 트윗인 경우 2개 트윗이 리스트로 걸림
            if str(type(tweet_text_div)) == "<class 'bs4.element.ResultSet'>":
                # print("list")
                try:
                    tweet_text_div = tweet_text_div[0]
                except IndexError:
                    pass

            tweet_writer = tweet_writer_span.text
            tweet_id = tweet_id_div.text
            tweet_datetime = str(tweet_datetime_a.find('time').attrs['datetime'])

            # print(type(tweet_text_div))
            try:
                tweet_text = tweet_text_div.text
            except AttributeError:
                tweet_text = ""

            result.append([tweet_writer]+[tweet_id]+[tweet_datetime]+[tweet_text])
        
        current_min_height = driver.execute_script("return document.body.scrollHeight")
        if current_min_height <= new_y + 1080:
            break
        current_y += 1080
    
    return


if __name__=="__main__":
    result = []
    print('Twitter crawling >>>>>>>>>>>>>>>>>>>>>>>')
    crawl(result)

    # 해당 attribute를 가진 데이터프레임 생성
    tbl = pd.DataFrame(result, columns={'writer', 'id', 'datetime', 'text'})

    # DataFrame to CSV file
    tbl.columns
    tbl.to_csv('./elon_twitter.csv', encoding='utf-8', mode='w', index=False)

    del result[:]