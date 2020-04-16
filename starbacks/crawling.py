from selenium import webdriver
from bs4 import BeautifulSoup

import re

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
# 혹은 options.add_argument("--disable-gpu")

driver = webdriver.Chrome('/Users/ensia96/Documents/chromedriver', options=options)

driver.implicitly_wait(1)

driver.get('https://www.starbucks.co.kr/menu/drink_list.do') # starbuck url 접근
bs = BeautifulSoup(driver.page_source, 'html.parser')


# 음료 카테고리의 제품군 list 리턴

def group_craw():
    target = bs.findAll('label',{'for':re.compile('product_*')})
    group_name = []
    for group in target:
        group_name.append(group.text)
    return group_name[1:] # ['콜드 브루 커피', '브루드 커피', '에스프레소', '프라푸치노', '블렌디드', '스타벅스 피지오', '티(티바나)', '기타 제조 음료', '스타벅스 주스(병음료)']


# 제품명, 영양정보 list 리턴

def product_name_ingredient_craw():
    target = bs.findAll('td')

    product = []
    kcal = []
    sugar = []
    protein = []
    sodium = []
    fat = []
    caffeine = []
    i = 0
    while i < len(target):
        product_name = target[i].text
        if (i % 7) == 0: # 7로 나눈 나머지가 0 -> 제품명 ( product )
            product.append(product_name)
        if (i % 7) == 1: # 7로 나눈 나머지가 1 -> 칼로리 ( kcal )
            kcal.append(product_name)
        if (i % 7) == 2: # 7로 나눈 나머지가 2 -> 당류 ( sugar )
            sugar.append(product_name)
        if (i % 7) == 3: # 7로 나눈 나머지가 3 -> 단백질 ( protein )
            protein.append(product_name)
        if (i % 7) == 4: # 7로 나눈 나머지가 4 -> 나트륨 ( sodium )
            sodium.append(product_name)
        if (i % 7) == 5: # 7로 나눈 나머지가 5 -> 포화지방 ( fat )
            fat.append(product_name)
        if (i % 7) == 6: # 7로 나눈 나머지가 6 -> 카페인 ( caffeine )
            caffeine.append(product_name)
        i += 1

driver.quit() # 안닫아주면 계속 창생겨서 렉걸림;