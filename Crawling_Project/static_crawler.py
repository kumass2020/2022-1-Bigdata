from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import datetime


def crawl():
    for page in range(1, 138):
        cs_url = 'https://www.gachon.ac.kr/cs/5905/subview.do?%d' % page
        print(cs_url)
        html = urllib.request.urlopen(cs_url)
        soup = BeautifulSoup(html, 'html.parser')
        tag_tbody = soup.find('tr')
        for content in tag_tbody.find_all('tr')[1:]:
            content_td = content[0].string
            content_subject = content[1].string.replace('N', '')
            content_writer = content[2].string
            content_date = content[3].string
            content_view = content[4].string
            content_comment = content[5].string
            content_file_num = content[6].string


if __name__=='__main__':
