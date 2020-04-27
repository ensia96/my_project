import time,re,csv

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
# 제품코드, 상품 이름, 가격 , 성별, 색상당 이미지 개수, 긴 설명, 큰 이미지

gijun = 'kids-shoes'
driver = webdriver.Chrome('/Users/ensia96/Documents/chromedriver')
#URL = "https://www.converse.co.kr/category/"+gijun
#driver.get(URL)

def scroll_down():
    SCROLL_PAUSE_TIME = 3

    last_height = driver.execute_script("return document.body.scrollHeight;")
    new_height = 0

    while True:
        for i in range(11):
            driver.execute_script(f"window.scrollTo({new_height}, document.body.scrollHeight * {i/10});")
            time.sleep(0.01)
        time.sleep(SCROLL_PAUSE_TIME)
        new_height = driver.execute_script("return document.body.scrollHeight;")

        if new_height == last_height:
            return True
        last_height = new_height

def get_product_codes():
    product_codes = []
    product_urls = driver.find_elements_by_class_name('product-url')
    for product_url in product_urls:
        url = product_url.get_attribute('href')
        product_codes.append(url.split('/')[-1])
    #driver.quit()

    return product_codes

def get_product_data(filename):
    BASE_URL = "https://www.converse.co.kr/product/"
    file = open(f'./data/{filename}_{gijun}.csv',mode='w',encoding='UTF-8',newline='')
    writer = csv.writer(file)
    writer.writerow(['code','size_list'])

    if scroll_down():
        product_codes = get_product_codes()
    
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    driver = webdriver.Chrome('/Users/ensia96/Documents/mydocs/chromedriver', options=options)

    for product_code in product_codes:
        driver.get(BASE_URL + product_code)
        button = driver.find_elements_by_xpath('//*[@id="wrapper"]/main/section/div[2]/div/div[4]/div/div[1]/a/span[1]')[0]
        button.click()
        try: # 모든 제품에 대해서 size 값이 정제되면, pk 값으로 변환예정
            size_container = driver.find_element_by_xpath('//*[@id="wrapper"]/main/section/div[2]/div/div[3]/div[2]/form/div[1]/div[4]/div/div')
            sizes = size_container.find_elements_by_tag_name('span')
            for size in sizes:
                writer.writerow([product_code,size.text])
        except NoSuchElementException:
            writer.writerow([product_code,'Free Size'])
        print(f'제품 : {product_code} ({product_codes.index(product_code)+1}/{len(product_codes)})')
    file.close()
    driver.quit()

def get_csv(): # 실루엣, 컬러 연결관계
    target = 'silhouette'
    newcsv = open(f"./data/{target}.csv", 'w+', encoding='utf-8')
    csv.writer(newcsv).writerow(['product_codes', target])

    silhouette_list = ['HIGH','LOW','MID','PLATFORM','SLIP']
    BASE_URL = 'https://www.converse.co.kr/category/shoes?style='

    for silhouette in silhouette_list:
        driver.get(BASE_URL + silhouette)
        product_codes = []
        if scroll_down():
            product_codes = get_product_codes()
            for code in product_codes:
                csv.writer(newcsv).writerow([code, silhouette])

    silhouette_list = ['HIGH','LOW','SLIP']
    BASE_URL = 'https://www.converse.co.kr/category/kids-shoes?style='

    for silhouette in silhouette_list:
        driver.get(BASE_URL + silhouette)
        product_codes = []
        if scroll_down():
            product_codes = get_product_codes()
            for code in product_codes:
                csv.writer(newcsv).writerow([code, silhouette])
    newcsv.close()

#    target = 'color'
#    newcsv = open(f"./data/{target}.csv", 'w+', encoding='utf-8')
#    csv.writer(newcsv).writerow(['product_codes', target])
#
#    color_list = ['000000','0000FF','009900','131936','6600CC','996633','999999','A39264','F0E4D2','FF0000','FF6600','FFB6C1','FFCC00','FFFFFF']
#    BASE_URL = 'https://www.converse.co.kr/category/shoes?color=%23'
#
#    for color in color_list:
#        driver.get(BASE_URL + color)
#        product_codes = []
#        if scroll_down():
#            product_codes = get_product_codes()
#            for code in product_codes:
#                csv.writer(newcsv).writerow([code, color])
#
#    color_list = ['000000','0000FF','009900','131936', '996633','999999', 'A39264','F0E4D2','FFFFFF']
#    BASE_URL = 'https://www.converse.co.kr/category/apparel-accessory?color=%23'
#
#    for color in color_list:
#        driver.get(BASE_URL + color)
#        product_codes = []
#        if scroll_down():
#            product_codes = get_product_codes()
#            for code in product_codes:
#                csv.writer(newcsv).writerow([code, color])
#
#    color_list = ['000000','131936', '999999','FF0000', 'FFB6C1', 'FFFFFF']
#    BASE_URL = 'https://www.converse.co.kr/category/kids-shoes?color=%23'
#
#    for color in color_list:
#        driver.get(BASE_URL + color)
#        product_codes = []
#        if scroll_down():
#            product_codes = get_product_codes()
#            for code in product_codes:
#                csv.writer(newcsv).writerow([code, color])
#    newcsv.close()

    driver.quit()

def get_instagram_data():
    file = open('converse_instagram.csv',mode='w',encoding='UTF-8',newline='')
    writer = csv.writer(file)
    writer.writerow(['thumbnail','profile_img','username','created_at'])
    driver.get('https://www.attractt.com/embed/grid/CCPPuTmry6XL961?loc=https://www.converse.co.kr/&target=attractt-ifm-0')
    time.sleep(4)
    button = driver.find_element_by_xpath('//*[@id="btn-view-more"]')
    button.click()
    time.sleep(3)

    contents = driver.find_element_by_xpath('//*[@id="contents"]')
    feeds = contents.find_elements_by_class_name('item-wrap')
    for feed in feeds:
        thumbnail = feed.find_element_by_class_name('thumbnail')
        profile = feed.find_element_by_class_name('overlay')
        profile_img = profile.find_element_by_class_name('user').find_element_by_tag_name('img').get_attribute('src')
        username = profile.find_element_by_class_name('info').find_element_by_class_name('username').text
        created_at = profile.find_element_by_class_name('info').find_element_by_class_name('time').text
        writer.writerow([thumbnail.get_attribute('src'),profile_img,username,created_at])

def get_store_info():
    driver.get('https://www.converse.co.kr/store')
    store_infos = driver.find_element_by_xpath('//*[@id="wrapper"]/main/article/div/div[2]/div[2]/div').get_attribute('data-store-list')
    print(store_infos)


#매장종류, 매장이름, 주소1, 주소2, 번호, 경도, 위도, 도시