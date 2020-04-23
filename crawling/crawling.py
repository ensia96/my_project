import time,re,csv

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
# 제품코드, 상품 이름, 가격 , 성별, 색상당 이미지 개수, 긴 설명, 큰 이미지

URL = "https://www.converse.co.kr/category/kids-shoes"
driver = webdriver.Chrome('/Users/ensia96/Documents/mydocs/chromedriver')
driver.get(URL)

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
    driver.quit()

    return product_codes

def get_product_data(filename):
    BASE_URL = "https://www.converse.co.kr/product/"
    file = open(f'product_{filename}.csv',mode='w',encoding='UTF-8',newline='')
    writer = csv.writer(file)
    writer.writerow(['code','name','price','gender','size_list','media_list','info_long','image_big'])

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
        product_name = driver.find_element_by_xpath('//*[@id="wrapper"]/main/section/div[2]/div/div[3]/div[2]/div[1]/h1').text
        price = driver.find_element_by_xpath('//*[@id="wrapper"]/main/section/div[2]/div/div[3]/div[2]/div[1]/p[1]/span').text
        price = price.split(' ')[0]
        price = re.sub(pattern = '[^\w\s]', repl = '', string = price) #,제거
        price = int(price)
        gender = driver.find_element_by_xpath('//*[@id="wrapper"]/main/section/div[2]/div/div[3]/div[2]/div[1]/p[2]').text
        product_info = driver.find_element_by_xpath('//*[@id="wrapper"]/main/section/div[2]/div/div[4]/div/div[1]/div')
        info_list = []
        p_tag = product_info.find_elements_by_tag_name('p')
        for p in p_tag:
            info_list.append(p.text)
        try:
            image_big = product_info.find_element_by_tag_name('img').get_attribute('src')
        except NoSuchElementException:
            image_big = None
        try: # 모든 제품에 대해서 size 값이 정제되면, pk 값으로 변환예정
            size_list = []
            size_container = driver.find_element_by_xpath('//*[@id="wrapper"]/main/section/div[2]/div/div[3]/div[2]/form/div[1]/div[4]/div/div')
            sizes = size_container.find_elements_by_tag_name('span')
            for size in sizes:
                size_list.append(size.text)
        except NoSuchElementException:
            size_list.append('Free Size')

        gallery = driver.find_element_by_xpath('//*[@id="wrapper"]/main/section/div[2]/div/div[2]/div[1]/div[2]/div[1]')
        images = gallery.find_elements_by_tag_name('img')
        videos = gallery.find_elements_by_tag_name('source')

        media_list = []
        for video in videos:
            media_list.append(video.get_attribute('src'))
        for image in images:
            image = image.get_attribute('src')
            media_list.append(image)

        writer.writerow([product_code,product_name,price,gender,size_list,media_list,info_list,image_big])
        print(f'제품 : {product_code} | {product_codes.index(product_code)+1}/{len(product_codes)}')
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

    target = 'color'
    newcsv = open(f"./data/{target}.csv", 'w+', encoding='utf-8')
    csv.writer(newcsv).writerow(['product_codes', target])

    color_list = ['000000','0000FF','009900','131936','6600CC','996633','999999','A39264','F0E4D2','FF0000','FF6600','FFB6C1','FFCC00','FFFFFF']
    BASE_URL = 'https://www.converse.co.kr/category/shoes?color=%23'

    for color in color_list:
        driver.get(BASE_URL + color)
        product_codes = []
        if scroll_down():
            product_codes = get_product_codes()
            for code in product_codes:
                csv.writer(newcsv).writerow([code, color])

    color_list = ['000000','0000FF','009900','131936', '996633','999999', 'A39264','F0E4D2','FFFFFF']
    BASE_URL = 'https://www.converse.co.kr/category/apparel-accessory?color=%23'

    for color in color_list:
        driver.get(BASE_URL + color)
        product_codes = []
        if scroll_down():
            product_codes = get_product_codes()
            for code in product_codes:
                csv.writer(newcsv).writerow([code, color])

    color_list = ['000000','131936', '999999','FF0000', 'FFB6C1', 'FFFFFF']
    BASE_URL = 'https://www.converse.co.kr/category/kids-shoes?color=%23'

    for color in color_list:
        driver.get(BASE_URL + color)
        product_codes = []
        if scroll_down():
            product_codes = get_product_codes()
            for code in product_codes:
                csv.writer(newcsv).writerow([code, color])
    newcsv.close()

    driver.quit()

def get_instagram_data():
    driver.get('https://www.converse.co.kr/')
    if scroll_down():
        user_name = driver.find_elements_by_class_name('thumbnail')
    print(user_name)

def get_store_info():
    driver.get('')
    store_infos = driver.find_element_by_xpath('//*[@id="wrapper"]/main/article/div/div[2]/div[2]/div')
    print(store_infos)