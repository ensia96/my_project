from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, csv
from datetime import datetime

def headless():
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    return options

#driver = webdriver.Chrome('/Users/ensia96/Documents/chromedriver', options=headless())
driver = webdriver.Chrome('/Users/ensia96/Documents/chromedriver')

def scroll_down(target): # 인자로 온 링크에 대해 스크롤다운
    driver.get(target)

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

def login(target):
    driver.get(target)
    a = driver.find_element_by_css_selector('#right-content > a')
    a.click()
    email = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input')
    click_next = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/span/span')
    email.send_keys('manchumgo@gmail.com')
    click_next.click()
    time.sleep(2)
    password = driver.find_element_by_css_selector('#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input')
    password.send_keys('akdrh1133!')
    time.sleep(2)
    driver.find_element_by_css_selector('#passwordNext > span').click()
    time.sleep(2)
    return True

def for_main(target):

    login(target)

    if scroll_down(target):

        for i in driver.find_elements_by_css_selector(
            '.previous-items-button.ytmusic-carousel, .next-items-button.ytmusic-carousel'
        ): # for click
            driver.execute_script("arguments[0].click();", i)
            time.sleep(0.1)

        for i in range(11): # for render
            driver.execute_script(f"window.scrollTo(0, document.body.scrollHeight * {i/10});")
            time.sleep(0.01)

    time.sleep(5)

    main = driver.find_element_by_css_selector('#contents.ytmusic-section-list-renderer')

    main_list = []

    if main.find_element_by_tag_name('picture').find_element_by_tag_name('img').get_attribute('src'):
        main_list.append({'main_thumb':main.find_element_by_tag_name('picture').find_element_by_tag_name('img').get_attribute('src')})

    source = main.find_elements_by_css_selector('#contents > ytmusic-immersive-carousel-shelf-renderer')
    source += main.find_elements_by_css_selector('#contents > ytmusic-carousel-shelf-renderer')

    when = datetime.today().strftime("%Y-%m-%d %H:%M") # 자동으로 오늘날짜를 지정해줘요!
    newcsv = open(f"./ym_data/{when}.csv", 'w+', encoding='utf-8')
    csv.writer(newcsv).writerow(['collection'])
    for sou in source: # 사용자 있을 때 리스트
        print(sou.find_element_by_tag_name('h2').get_attribute('aria-label'))
        csv.writer(newcsv).writerow([sou.find_element_by_tag_name('h2').get_attribute('aria-label')])
    newcsv.close()

#    for sou in source:
#        main_list.append(
#            {
#                'collection ': sou.find_element_by_tag_name('h2').get_attribute('aria-label'),
#                'elements   ': [
#                    {
#                        'thumb':h.find_element_by_id('img').get_attribute('src'),
#                        'name':h.find_element_by_css_selector('.image-wrapper').get_attribute('title'),
#                        'link':h.find_element_by_css_selector('.image-wrapper').get_attribute('href'),
#                        'type':h.find_element_by_css_selector('.subtitle').text[
#                            :h.find_element_by_css_selector('.subtitle').text.find('•')-1],
#                        'artist':{
#                            'name':h.find_element_by_css_selector('.subtitle').text[
#                                h.find_element_by_css_selector('.subtitle').text.find('•')+2:],
##                            'link':[
##                                h.find_elements_by_css_selector('a.yt-formatted-string')[1].get_attribute('href')
##                                if len(h.find_elements_by_css_selector('a.yt-formatted-string')) > 1 else None
##                            ]
#                        }
#                    }
#                    for i in sou.find_elements_by_tag_name('ul')
#                    for h in i.find_elements_by_css_selector('ytmusic-two-row-item-renderer')
#                ]
#            }
#        )
#    print(main_list)

    driver.quit()

def for_hotlist(target):

    hotlist = driver.find_elements_by_css_selector('ytmusic-full-bleed-item-renderer')

    hot_list = [
        {
            'thumbnail':hot.find_element_by_css_selector('img.yt-img-shadow').get_attribute('src'),
            'song_name':hot.find_element_by_css_selector('.title.ytmusic-full-bleed-item-renderer').text,
            'artist':hot.find_element_by_css_selector(
                '.subtitle.ytmusic-full-bleed-item-renderer'
            ).get_attribute('title')[
                :hot.find_element_by_css_selector(
                    '.subtitle.ytmusic-full-bleed-item-renderer'
                ).get_attribute('title').find('•')-1
            ],
            'views':hot.find_element_by_css_selector(
                '.subtitle.ytmusic-full-bleed-item-renderer'
            ).get_attribute('title')[
                hot.find_element_by_css_selector(
                    '.subtitle.ytmusic-full-bleed-item-renderer'
                ).get_attribute('title').find('•')+6:-1
            ]
        }
        for hot in hotlist
    ]

    print(hot_list)

    driver.quit()

def for_artist(target):
    target = 'https://music.youtube.com/tasteprofile'


#############################################################################################

for_main('https://music.youtube.com')

#for_hotlist('https://music.youtube.com/hotlist')

#driver.quit()
