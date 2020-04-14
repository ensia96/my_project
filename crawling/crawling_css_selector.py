from bs4 import BeautifulSoup # beautifulsoup 모듈 참조
from urllib.request import urlopen # urllib 의 request 항목에서 urlopen 참조
import re # re 모듈 참조 ( regular expression / 정규표현식 )

import requests # requests 모듈 참조 -> url 정보를 get 방식으로 처리하기 위해

# 1. 대상 URL 지정
crawling_url = "http://www.vogue.co.kr/category/fashion/page/1"

# 2. 대상 URL 상태 변환 ( 문서를 연 상태로 )
html_doc = urlopen(crawling_url)

# 3. 위에서 지정한 html 변수내용과 html.parser 라는 처리방식 개채를 매개변수로 지정하여 beautifulsoup 가 처리하도록 하는 호출자 지정
bs = BeautifulSoup(html_doc.read(), 'html.parser')

# 4. 위에서 지정한 처리방식으로 처리된 데이터 중에서 css 선택자에 해당하는 정보만을 원하는 변수에 할당
post_select = bs.select("#post-219030 > div > div.fusion-post-content-wrapper > div.fusion-post-content.post-content > h2 > a")