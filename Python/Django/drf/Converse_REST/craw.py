from selenium import webdriver
import os, time, csv
from datetime import datetime


def headless():
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    options.add_argument("window-size=1920x1080")
    options.add_argument("disable-gpu")
    return options


# driver = webdriver.Chrome('/Users/ensia96/Documents/chromedriver', options=headless())
driver = webdriver.Chrome("chromedriver")

link = "https://www.converse.co.kr/category/shoes"


def scroll_down(target):  # 인자로 온 링크에 대해 스크롤다운
    driver.get(target)

    SCROLL_PAUSE_TIME = 3

    last_height = driver.execute_script("return document.body.scrollHeight;")
    new_height = 0

    while True:
        for i in range(11):
            driver.execute_script(
                f"window.scrollTo({new_height}, document.body.scrollHeight * {i/10});"
            )
            time.sleep(0.01)
        time.sleep(SCROLL_PAUSE_TIME)
        new_height = driver.execute_script("return document.body.scrollHeight;")

        if new_height == last_height:
            return True
        last_height = new_height


def for_products(target):
    scroll_down(target)

    time.sleep(5)

#    main = driver.find_element_by_css_selector("")
#    source = main.find_elements_by_css_selector()
#    source += main.find_elements_by_css_selector()
    print('haha')


for_products(link)

driver.quit()
