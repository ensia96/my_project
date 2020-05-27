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

def get_product_data():
    BASE_URL = "https://www.converse.co.kr/product/"
    file = open('converse_shoes_test.csv',mode='w',encoding='UTF-8',newline='')
    writer = csv.writer(file)
    writer.writerow(['code','name','price','gender','summary','color_name','series_list','series_img_list','size_list','media_list','info_long','image_big'])

    if scroll_down():
        product_codes = get_product_codes()
    #product_codes = ['167826C']
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
        try:
            summary = driver.find_element_by_class_name('product-description').text
        except NoSuchElementException:
            summary = None
        color_name = driver.find_element_by_xpath('//*[@id="wrapper"]/main/section/div[2]/div/div[3]/div[2]/form/div[1]/div[1]/div[1]/span[2]').text
        series_list = []
        series_img_list = []
        series_container = driver.find_element_by_xpath('//*[@id="wrapper"]/main/section/div[2]/div/div[3]/div[2]/form/div[1]/div[2]')
        series = series_container.find_elements_by_class_name('selectable')
        for shoe in series:
            series_list.append(shoe.find_element_by_tag_name('a').get_attribute('href').split('/')[-1])
            series_img_list.append(shoe.find_element_by_tag_name('img').get_attribute('src'))
        product_info = driver.find_element_by_xpath('//*[@id="wrapper"]/main/section/div[2]/div/div[4]/div/div[1]/div')
        info_list = []
        p_tag = product_info.find_elements_by_tag_name('p')
        for p in p_tag:
            info_list.append(p.text)
        try:
            image_big = product_info.find_element_by_tag_name('img').get_attribute('src')
        except NoSuchElementException:
            image_big = None
        try:
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

        writer.writerow([product_code,product_name,price,gender,summary,color_name,series_list,series_img_list,size_list,media_list,info_list,image_big])

def get_silhouette_product():
    silhouette_list = ['HIGH','LOW','MID','PLATFORM','SLIP']
    BASE_URL = 'https://www.converse.co.kr/category/shoes?style='
    silhouette_code_dict = {}
    for silhouette in silhouette_list:
        driver.get(BASE_URL + silhouette)
        product_codes = []
        if scroll_down():
            product_codes = get_product_codes()
            silhouette_code_dict[silhouette] = product_codes
    print(silhouette_code_dict)

def get_color_product():
    color_list = ['23000000','230000FF','23009900','23131936','236600CC','23996633','23999999','23A39264','23F0E4D2','23FF0000','23FF6600','23FFB6C1','23FFCC00','23FFFFFF']
    BASE_URL = 'https://www.converse.co.kr/category/shoes?color=%'
    color_code_dict = {}
    for color in color_list:
        driver.get(BASE_URL + color)
        product_codes = []
        if scroll_down():
            product_codes = get_product_codes()
            color_code_dict[color[2::]] = product_codes
    print(color_code_dict)

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
#get_product_data()