from bs4 import BeautifulSoup
import pandas as pd
import requests
import re


# 정규표현식 사용 
def regularize(str1):
    # str2 = str1
    # str3 = str(str2).strip()
    # if str2 == None:
    #     pass
    # else:
    #     str4 = ' '.join(str2.split())

    # return re.sub('[^0-9a-zA-Zㄱ-힗.\s]','',str(str1))
    if str1 == None:
        return None
    else:
        return ' '.join(str1.split())

# 크롤링 수행
def crawl(result):
    for page in range(1, 138):
        # URL 지정
        cs_url = 'https://www.gachon.ac.kr/cs/5905/subview.do?page=%d' % page
        print(cs_url)

        # requests, BeautifulSoup 객체 호출
        # html = urllib.request.urlopen(cs_url)
        html = requests.get(cs_url).text
        soup = BeautifulSoup(html, 'html.parser')

        # tbody 태그로 검색
        tag_tbody = soup.find('tbody')

        # tbody 태그 하위 tr 태그를 (첫번째 요소 제외하고) 모두 찾음
        for parent_content in tag_tbody.find_all('tr')[1:]:
            # tr 태그 하위 td 태그를 모두 찾음
            content = parent_content.find_all('td')
            # 게시물의 각 정보를 string 형태로 저장
            content_id = regularize(content[0].string)
            content_subject = regularize(content[1].text).rstrip('N')    # 필요없는 텍스트 제거
            content_writer = regularize(content[2].string)
            content_date = regularize(content[3].string)
            content_view = regularize(content[4].string)
            content_comment = regularize(content[5].string)
            content_file_num = regularize(content[6].string)
            # result 배열에 저장
            result.append([content_id]+[content_subject]+[content_writer]+[content_date]
                        +[content_view]+[content_comment]+[content_file_num])
    return

if __name__=='__main__':
    result = []
    print('Gachon CS Notice crawling >>>>>>>>>>>>>>>>>>>>>>>>')
    crawl(result)

    # 해당 attribute를 가진 데이터프레임 생성
    tbl = pd.DataFrame(result, columns={'id', 'subject', 'writer', 'date', 'view', 'comment', 'file'})

    # DataFrame to CSV file

    tbl.columns
    tbl.to_csv('./Gachon_CS_Notice.csv', encoding='utf-8', mode='w', index=False)

    del result[:]
