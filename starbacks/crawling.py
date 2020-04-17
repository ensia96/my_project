from selenium import webdriver
from bs4 import BeautifulSoup
import re

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
# 혹은 options.add_argument("--disable-gpu")
driver = webdriver.Chrome('/Users/ensia96/Documents/mydocs/chromedriver', options=options)
driver.implicitly_wait(1)

def get_source(i): # 소스 받아오는 데코레이터  'https://www.starbucks.co.kr/menu/drink_list.do'
    def deco_func(func):
        def get():
            driver.get(i) # starbuck url 접근
            bs = BeautifulSoup(driver.page_source, 'html.parser')
            return func(bs)
        return get
    return deco_func

@get_source('https://www.starbucks.co.kr/menu/drink_list.do')
def group_craw(bs): # 음료 카테고리의 제품군 list 리턴
    target = bs.findAll('label',{'for':re.compile('product_*')})
    group_name = []
    for group in target:
        group_name.append(group.text)
    return group_name[1:]


@get_source('https://www.starbucks.co.kr/menu/drink_list.do')
def product_name_ingredient_craw(bs):# 제품명, 영양정보 list 리턴
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

@get_source('https://www.starbucks.co.kr/menu/drink_list.do')
def mk_prod_list(func): # 제품 id list 를 돌려주는 데코레이터
    def prod_id(bs):
        target = bs.findAll('a', {'class':'goDrinkView'})
        product_id=[]
        for i in range(len(target)):
            product_id.append(target[i]['prod'])
        return func(product_id)
    return prod_id

#@mk_prod_list
#def test(i):
#    print(i)


#name_en = []
#description = []
#for ids in product_id:
#    driver.get(f'https://www.starbucks.co.kr/menu/drink_view.do?product_cd={ids}')
#    soe = BeautifulSoup(driver.page_source, 'html.parser')
#    desc_top = driver.find_element_by_class_name('t1')
#    desc_btm = driver.find_element_by_class_name('product_view_wrap2')
#    description.append(desc_top.text)
#    description.append(desc_btm.text)
#
#print(len(description))




driver.quit() # 안닫아주면 계속 창생겨서 렉걸림;
