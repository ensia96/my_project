from selenium import webdriver
from bs4 import BeautifulSoup
import re, csv

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
# 혹은 options.add_argument("--disable-gpu")
driver = webdriver.Chrome('/Users/ensia96/Documents/mydocs/chromedriver', options=options)
driver.implicitly_wait(1)

def get_source(i): # 소스 받아오는 데코레이터
    def deco_func(func):
        def get():
            driver.get(i)
            bs = BeautifulSoup(driver.page_source, 'html.parser')
            return func(bs)
        return get
    return deco_func

@get_source('https://www.starbucks.co.kr/menu/drink_list.do')
def mk_prodlist(bs): # 제품 id list 를 돌려주는 데코레이터
    def prod_list(func):
        def prod_id():
            target = bs.findAll('a', {'class':'goDrinkView'})
            product_id=[]
            for i in range(len(target)):
                product_id.append(target[i]['prod'])
            return func(product_id)
        return prod_id
    return prod_list

# newcsv = open("../data/파일명.csv", 'w+', encoding='utf-8')
# csv.writer(newcsv).writerow(('항목','항목1'))
# newcsv.close()

def write_csv(filename, cols, rows): # csv 자동 분류작성 함수 ( 수정 중 )
    newcsv = open(f"../data/{filename}.csv", 'w+', encoding='utf-8')
    csv.writer(newcsv).writerow(cols)
    for i in range(len(rows)):
        print(i)
    newcsv.close()

@get_source('https://www.starbucks.co.kr/menu/drink_list.do')
def product_name_ingredient_craw(bs):# 제품명, 영양정보
    target = bs.findAll('td') # list 추가 대신 db에 삽입방식으로 변경 예정

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
    return (kcal, sugar, protein, sodium, fat, caffeine)

def test1(): # 영양정보 테이블 (kcal, sugar, protein, sodium, fat, caffeine)
    a = product_name_ingredient_craw()
    for i in range(len(a[0])):
        b = (a[0][i],a[1][i],a[2][i],a[3][i],a[4][i],a[5][i])
        print(b)

#test1()

# //*[@id="product_info01"]

@mk_prodlist()
def test(product): # 테스트 용 함수
    ids = product[0]
    driver.get(f'https://www.starbucks.co.kr/menu/drink_view.do?product_cd={ids}')
    aa = driver.find_element_by_xpath('/html/body/div[3]/div[7]/div[1]/div/h2/img').get_attribute('alt')
    print(aa)

# groupname = driver.find_element_by_xpath('/html/body/div[3]/div[7]/div[1]/div/h2/img').get_attribute('alt')
    # 그룹이름 group id 값으로 변환 필요함

@mk_prodlist()
def testing(product):
    name_en = []
    description = []
    size_set = []
    for ids in product:
        driver.get(f'https://www.starbucks.co.kr/menu/drink_view.do?product_cd={ids}')
        # if 
        en = driver.find_element_by_xpath('/html/body/div[3]/div[7]/div[2]/div[1]/div[2]/div[1]/h4/span')
        # desc_top = driver.find_element_by_class_name('t1')
        # size = driver.find_element_by_xpath('/html/body/div[3]/div[7]/div[2]/div[1]/div[2]/form/fieldset/div/div[1]/div/div[1]')
        # desc_btm = driver.find_element_by_class_name('product_view_wrap2')
        name_en.append(en.text)
        # description.append(desc_top.text)
        # size_set.append(size.text)
        # description.append(desc_btm.text)
    return name_en


driver.quit() # 안닫아주면 계속 창생겨서 렉걸림;
