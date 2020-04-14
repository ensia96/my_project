from bs4 import BeautifulSoup # beautifulsoup 모듈 참조
from urllib.request import urlopen # urllib 의 request 항목에서 urlopen 참조
import csv # csv 모듈 참초
import re # re 모듈 참조 ( regular expression / 정규표현식 ) -> compile 기능을 위해
import requests # requests 모듈 참조 -> url 정보를 get 방식으로 처리하기 위해

# 1. csv 관리방식 정의 및 table attribute 정의

# 1 - 1 . csv 파일 생성 ( 이름지정 )
csv_filename_to_write = "fasion_all.csv"

# 1 - 2 . csv 파일을 여는 호출자 정의 ( 대상파일, 권한, 메타정보를 인자로 받아 참조 / 타겟파일, write ( 쓰기 ), ' utf-8 서식 문서데이터 ' )
csv_open = open(csv_filename_to_write, 'w+', encoding='utf-8')

# 1 - 3 . csv 에 문서작성을 하는 호출자 정의 ( 파일을 여는 호출자를 인자로 받아 참조 )
csv_writer = csv.writer(csv_open)

# 1 - 4 . csv 문서작성 호출자의 내장함수 writerow 를 호출하여 table 의 attribute 를 지정
csv_writer.writerow(('title','image_url'))



# 2. BeautifulSoup 동작방식 정의

# 2 - 1 . 대상 URL 지정
crawling_url = "http://www.vogue.co.kr/category/fashion/page/1"

# 2 - 2 . 대상 url 의 정보를 get 요청방식으로 받아오는 호출자 지정
req = requests.get(crawling_url)

# 2 - 3 . 위의 호출자로 받아온 정보를 내장함수 text 로 호출하여, html 이라는 변수에 할당
html = req.text

# 2 - 4 . 위에서 지정한 html 변수내용과 html.parser 라는 처리방식 개채를 매개변수로 지정하여 beautifulsoup 가 처리하도록 하는 호출자 지정
bs = BeautifulSoup(html, 'html.parser')


# 3. Resource 의 재분배 ( 원하는 정보형태로 가공 )

# 3 - 1 . bueutifulsoup 가 추출해낸 정보들을 (article, json (id : post-* (포스트 전체에 대한 패턴 객체)) 형태로 만들어 list 화
article_list = bs.findAll('article', {'id': re.compile('post-*')})

# 3 - 2 . 위의 추출된 데이터 목록에 대하여 반복구문 정의
for article in article_list:

    # 3 - 2 - 1 . 추출된 데이터에서 title 값 추출하기
    h2_title = article.findAll('h2') # h2_title 변수에 article 객체 중 ' h2 태그를 가진 ' 요소들을 할당
    title = h2_title[0].text # title 변수에 h2 태그를 가진 정보 중 제일 처음오는 정보를 할당
    title = " ".join(title.split()) # 정보를 보기좋은 문자열로 변환

    # 3 - 2 - 2 . 추출된 데이터에서 img src 값 추출하기
    img = article.find('img') # img 변수에 article 객체 중 ' img 태그를 가진 ' 요소를 할당
    image_url = img['src'] # image_url 변수에 img 의 src 속성부분 정보를 할당 ( 이때, 추출된 img 는 dict 형태 )

    # 3 - 2 - 3 . 정제된 데이터를 기반으로 csv 내용 작성
    csv_writer.writerow((title, image_url))

# 4 . 원하는 동작이 마무리 되었으니, 파일을 닫음
csv_open.close()