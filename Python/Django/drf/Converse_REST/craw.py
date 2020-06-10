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

link = "https://www.converse.co.kr"


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


def categories_groups(target):
    driver.get(target)
    time.sleep(5)

    categories = driver.find_elements_by_class_name("anchor.level-1")
    groups = driver.find_elements_by_class_name("anchor.level-2")

    category_group = []

    for category in categories:
        if category.text:
            if "link" not in category.get_attribute("class"):
                cat_gro = {"category": category.text, "groups": []}
                category.click()
                time.sleep(2)
                for group in groups:
                    if group.text:
                        cat_gro["groups"].append(
                            {
                                "name": group.text,
                                "link": group.get_attribute("href").split("/")[-1],
                            }
                        )
                category_group.append(cat_gro)
            # else:
            #     category_group.append(
            #         {
            #             "category": category.text,
            #             "link": category.get_attribute("href").split("/")[-1],
            #         }
            #     )

    print(category_group)

    for element in category_group:
        for group in element["groups"]:
            products(link + "/category/" + group["link"])
            time.sleep(2)


def products(target):
    driver.get(target)
    if driver.find_elements_by_xpath(
        "/html/body/section/main/section/div[1]/div[2]/div[1]/div[1]"
    ):
        print(
            driver.find_elements_by_xpath(
                "/html/body/section/main/section/div[1]/div[2]/div[1]/div[1]"
            )[0]
            .find_element_by_tag_name("img")
            .get_attribute("src")
        )
    # scroll_down(target)
    time.sleep(2)


categories_groups(link)

# print(os.getcwd())
# print(os.listdir())

driver.quit()
