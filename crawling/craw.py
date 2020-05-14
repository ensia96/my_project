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

    driver.find_element_by_css_selector('#right-content > a').click()

    driver.find_element_by_css_selector('#identifierId').send_keys('manchumgo@gmail.com')
    driver.find_element_by_css_selector('#identifierNext > span > span').click()
    time.sleep(2)

    driver.find_element_by_css_selector('#password > div > div > div > input').send_keys('akdrh1133!')
    time.sleep(2)
    driver.find_element_by_css_selector('#passwordNext > span').click()
    time.sleep(2)

    return True

def item_render():

    for i in driver.find_elements_by_css_selector(
        '.previous-items-button.ytmusic-carousel, .next-items-button.ytmusic-carousel'
    ):
        driver.execute_script("arguments[0].click();", i)

        time.sleep(0.1)

    for i in range(11):
        driver.execute_script(f"window.scrollTo(0, document.body.scrollHeight * {i/10});")
        time.sleep(0.01)

    return True

def for_main(target):

    login(target)

    scroll_down(target)

    item_render()

    time.sleep(5)

    main = driver.find_element_by_css_selector('#contents.ytmusic-section-list-renderer')

    main_list = []

#    if main.find_element_by_tag_name('picture').find_element_by_tag_name('img').get_attribute('src'):
#
#        main_list.append(
#            {
#                'main_thumb':main.find_element_by_tag_name(
#                    'picture'
#                ).find_element_by_tag_name(
#                    'img'
#                ).get_attribute('src')
#            }
#        )

    source = main.find_elements_by_css_selector('#contents > ytmusic-immersive-carousel-shelf-renderer')
    source += main.find_elements_by_css_selector('#contents > ytmusic-carousel-shelf-renderer')

#    when = datetime.today().strftime('%Y-%m-%d %H:%M')
#    newcsv = open(f"./ym_data/{when}.csv", 'w+', encoding='utf-8')
#
#    for sou in source:
#
#        print(
#            sou.find_element_by_tag_name('h2').get_attribute('aria-label')+" 이(가) 작성됨"
#        )
#
#        csv.writer(newcsv).writerow([
#            sou.find_element_by_tag_name('h2').get_attribute('aria-label')
#        ])
#
#    newcsv.close()

    for sou in source:

#        main_list.append(
#            {
#                'collection': sou.find_element_by_tag_name('h2').get_attribute('aria-label'),
#                'elements': [
#                    {
#                        'name':h.find_element_by_css_selector('.image-wrapper').get_attribute('title'),
#                        'link':h.find_element_by_css_selector('.image-wrapper').get_attribute('href'),
#                    }
#                    for i in sou.find_elements_by_tag_name('ul')
#                    for h in i.find_elements_by_css_selector('ytmusic-two-row-item-renderer')
#                ]
#            }
#        )

        for i in sou.find_elements_by_tag_name('ul'):
            for h in i.find_elements_by_css_selector('ytmusic-two-row-item-renderer'):
                main_list.append(h.find_element_by_css_selector('.image-wrapper').get_attribute('href'))

   for element in main_list:
       for_list(element)
       print(main_list[element]+'/'+len(main_list))

    print('끝!')

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

def for_list(target):

    scroll_down(target)

    time.sleep(2)

    list_header = driver.find_element_by_css_selector('ytmusic-detail-header-renderer')

    list_thumb = list_header.find_element_by_tag_name('img').get_attribute('src')
    list_title = list_header.find_element_by_class_name('title').text

    print(list_title)


    list_sub = list_header.find_element_by_class_name('subtitle')

    type = list_sub.text[
        :list_sub.text.find('•')-1
    ]
    artist = {
        'name':list_sub.text[list_sub.text.find('•')+2:-7],
        'link':''
    }
    if 0<len(
        list_sub.find_elements_by_css_selector('a.yt-simple-endpoint')
    ):
        artist['link']=list_sub.find_element_by_css_selector(
            'a.yt-simple-endpoint'
        ).get_attribute('href')
    year = list_sub.text[-4:]


    list_ssub = list_header.find_element_by_class_name('second-subtitle').text

    number = list_ssub[3:list_ssub.find('곡')]
    fulltime = list_ssub[list_ssub.find('•')+2:]
    length = {}
    if '시간' in fulltime:
        length['hour'] = fulltime[:fulltime.find('시')]
    length['minute'] = fulltime[-3:-1]


    description = list_header.find_element_by_css_selector('.description').text


    itemlist = driver.find_elements_by_css_selector('ytmusic-responsive-list-item-renderer')

    for i in itemlist:
        thumb = i.find_element_by_tag_name('img').get_attribute('src')
        title = i.find_element_by_class_name('title').text
        artist = i.find_elements_by_class_name('flex-column')[0].get_attribute('title')
        album = i.find_elements_by_class_name('flex-column')[1].get_attribute('title')
        length = i.find_element_by_class_name('fixed-column').text

def for_artist(target):
    target = 'https://music.youtube.com/tasteprofile'

#############################################################################################

for_main('https://music.youtube.com')

#for_hotlist('https://music.youtube.com/hotlist')

#for_list('https://music.youtube.com/playlist?list=rdclak5uy_ln9xj1rqgmbltmvrztvhmg-vyvt594kyu') # 구글 DB에서 폐기함
#for_list('https://music.youtube.com/playlist?list=PLWImZYQw4M8ePtdzPMzkeJtuzF9qVchBR')
#for_list('https://music.youtube.com/playlist?list=RDCLAK5uy_kfdjbDJHQEj3DMdo5Qt6hlP-dxVRL26tM')

#more_test('https://music.youtube.com/channel/UCa5qWh5TRLCVFkCO67_gOtw')
#more_test('https://music.youtube.com/playlist?list=RDCLAK5uy_kx8KLdeTpmUxdsdetXKOkT07jEVp2LhDE')

driver.quit()
