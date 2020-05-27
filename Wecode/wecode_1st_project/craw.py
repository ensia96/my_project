from selenium import webdriver
from bs4 import BeautifulSoup
import re, csv, time

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")

# 함수 새로 만들면, 끝에 항상 'driver.quit()' 붙이기

# shoes
    # chucktaylorallstar, chuck70, onestar, jackpurcell
# apparel-accessory
    # tops, pants, accessory
# kids-shoes
    # baby-shoes, kids
taarget = 'group'
gijun = 'kids'
pk=9
source=[
"https://www.converse.co.kr/category/"+gijun,
'a',
{'class':'product-url'},
'href',
taarget+'_'+gijun,
['product_id',taarget],
'https://www.converse.co.kr/product/'
]

def scroll_down(source): # 스크롤 다운 후 소스 반환
    def deco_func(func):
        def get():
            driver = webdriver.Chrome('/Users/ensia96/Documents/chromedriver')
            driver.get(source[0])
            last_height = driver.execute_script("return document.body.scrollHeight;")
            new_height = 0
            while True:
                for i in range(11):
                    driver.execute_script(f"window.scrollTo({new_height}, document.body.scrollHeight * {i/10});")
                    time.sleep(0.01)
                time.sleep(3)
                new_height = driver.execute_script("return document.body.scrollHeight;")
                if new_height == last_height:
                    source.append(BeautifulSoup(driver.page_source, 'html.parser'))
                    driver.quit()
                    return func(source)
                last_height = new_height
        return get
    return deco_func

@scroll_down(source)
def target_list(source): # 소스에서 원하는 항목 목록 반환
    def prod_list(func):
        def prod_id():
            target = source[-1].findAll(source[1], source[2])
            product_id=[]
            for i in range(len(target)):
                product_id.append(target[i][source[3]].split('/')[-1])
                source.append(product_id)
            return func(source)
        return prod_id
    return prod_list

def return_list(): # 제품id 리스트 반환용 함수
    return source[-1]

@target_list()
def for_project(source): # 프로젝트용 함수
    print(f'{len(source[-1])}')
    newcsv = open(f"./data/group/{source[4]}.csv", 'w+', encoding='utf-8')
    csv.writer(newcsv).writerow(source[5])
    driver = webdriver.Chrome('/Users/ensia96/Documents/chromedriver', options=options)
    driver.implicitly_wait(1)
    # 정보분류 정의는 craw_test 에서 붙여넣기
    for ids in source[-1]:
        csv.writer(newcsv).writerow([ids,pk])
        print(f'제품 : {ids} ( {source[-1].index(ids)+1}/{len(source[-1])} )')
    print('정보 분류 완료')
    newcsv.close()
    driver.quit()

#############################################################################################

for_project()


###################################### 연 구 중 ###############################################

# def find_text(product): # 태그의 text 정보를 추출하고 싶을 때 쓰는 함수
#     driver = webdriver.Chrome('/Users/ensia96/Documents/mydocs/chromedriver', options=options)
#     driver.implicitly_wait(1)
#     testing = []
#     for ids in product:
#         driver.get(f'{link}{ids}')
#         testing.append(driver.find_element_by_xpath(xpath).text)
#     return testing

# def find_attr(product): # 태그의 특정 속성값을 추출하고 싶을 때 쓰는 함수
#     driver = webdriver.Chrome('/Users/ensia96/Documents/mydocs/chromedriver', options=options)
#     driver.implicitly_wait(1)
#     testing = []
#     for ids in product:
#         driver.get(f'{link}{ids}')
#         testing.append(driver.find_element_by_xpath(xpath).get_attribute(need_attr))
#     return testing
