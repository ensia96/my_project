from bs4 import BeautifulSoup
import re
import requests

crawling_url = "http://www.vogue.co.kr/category/fashion/"

req = requests.get(crawling_url)
html = req.text

# print(html) -> html 문서내용쓰

bs = BeautifulSoup(html,'html.parser')

article_list = bs.findAll('article', {'id': re.compile('post-*')})

for article in article_list:
    h2_title = article.findAll('h2')
    title = h2_title[0].text
    # print(title)
    title = " ".join(title.split())


# 마지막 질문
# findAll 에 인자로 오는 친구들