from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv, re, requests

newcsv = open("../data/billboard_100.csv", 'w+', encoding='utf-8')

csv.writer(newcsv).writerow(('rank','name', 'artist'))

bs = BeautifulSoup(requests.get("https://www.billboard.com/charts/hot-100").text, 'html.parser')

billboard = bs.findAll('ol', {'class' : 'chart-list__elements'})

for bill in billboard:
    billname = bill.findAll('span', {'class':"chart-element__information__song text--truncate color--primary"})
    billarti = bill.findAll('span', {'class':"chart-element__information__artist text--truncate color--secondary"})
    for i in range(100):
        rank = i+1
        name = billname[i].text
        arti = billarti[i].text
        csv.writer(newcsv).writerow((rank, name, arti))

newcsv.close()

# 성공, 결과파일 = ../data/billboard_100.csv