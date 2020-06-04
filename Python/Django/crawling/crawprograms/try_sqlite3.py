from bs4 import BeautifulSoup
from urllib.request import urlopen
import sqlite3, re, requests

#with sqlite3.connect('database.db') as conn: -> 배워볼것
#    c = conn.cursor()

conn = sqlite3.connect('../data/billboard_100.sqlite3')
c = conn.cursor()

# 테이블 생성 구문 실행
c.execute('''CREATE TABLE top100 (rank, name, artist)''')

bs = BeautifulSoup(requests.get("https://www.billboard.com/charts/hot-100").text, 'html.parser')

billboard = bs.findAll('ol', {'class' : 'chart-list__elements'})

for bill in billboard:
    billname = bill.findAll('span', {'class':"chart-element__information__song text--truncate color--primary"})
    billarti = bill.findAll('span', {'class':"chart-element__information__artist text--truncate color--secondary"})
    for i in range(100):
        name = billname[i].text
        arti = billarti[i].text
        # 내용 삽입 구문 실행
        c.execute(f"""insert into top100 (rank, name, artist) values ("{i+1}","{name}", "{arti}")""")

# 변경사항 적용
conn.commit()

# 종료
conn.close()

# 성공, 결과파일 = ../data/billboard_100.sqlite3