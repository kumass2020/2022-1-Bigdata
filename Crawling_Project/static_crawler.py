from bs4 import BeautifulSoup
import urllib.request
import pandas as pd


# 크롤링 수행
def crawl(result):
    for page in range(1, 138):
        # URL 지정
        cs_url = 'https://www.gachon.ac.kr/cs/5905/subview.do?%d' % page
        print(cs_url)

        # urllib, BeautifulSoup 객체 호출
        html = urllib.request.urlopen(cs_url)
        soup = BeautifulSoup(html, 'html.parser')

        # tbody 태그로 검색
        tag_tbody = soup.find('tbody')

        # tbody 태그 하위 tr 태그를 (첫번째 요소 제외하고) 모두 찾음
        for content in tag_tbody.find_all('tr')[1:]:
            # 게시물의 각 정보를 string 형태로 저장
            content_id = content[0].string
            content_subject = content[1].string.replace('N', '')    # 필요없는 텍스트 제거
            content_writer = content[2].string
            content_date = content[3].string
            content_view = content[4].string
            content_comment = content[5].string
            content_file_num = content[6].string
            # result 배열에 저장
            result.append([content_id]+[content_subject]+[content_writer]+[content_date]
                        +[content_view]+[content_comment]+[content_file_num])
    return

if __name__=='__main__':
    result = []
    print('Gachon CS crawling >>>>>>>>>>>>>>>>>>>>>>>>')
    crawl(result)

    # 해당 attribute를 가진 데이터프레임 생성
    tbl = pd.DataFrame(result, columns={'id', 'subject', 'writer', 'date', 'view', 'comment', 'file'})

    # DataFrame to CSV file
    tbl.to_csv('./Gachon_CS_Notice.csv', encoding='cp949', mode='w', index=True)

    del result[:]
