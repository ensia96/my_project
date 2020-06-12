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
    SCROLL_PAUSE_TIME = 3
    driver.get(target)
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


def initialize_db(target):
    driver.get(target)
    time.sleep(5)

    categories = driver.find_elements_by_class_name("anchor.level-1")
    sub_categories = driver.find_elements_by_class_name("anchor.level-2")

    category_list = []

    for category in categories:
        if category.text:
            if "link" not in category.get_attribute("class"):
                cat_gro = {"category": category.text, "sub_categories": []}
                category.click()
                time.sleep(2)
                for group in sub_categories:
                    if group.text:
                        # if group.text != "회원전용":
                        cat_gro["sub_categories"].append(
                            {
                                "name": group.text,
                                "link": group.get_attribute("href").split("/")[-1],
                            }
                        )
                category_list.append(cat_gro)

            # this is for uncategorized sub_categories
            # else:
            #     category_list.append(
            #         {
            #             "category": category.text,
            #             "link": category.get_attribute("href").split("/")[-1],
            #         }
            #     )

    print("카테고리와 그룹에 대한 분별이 끝났습니다.")

    group_product = []

    element = category_list[2]
    # for element in category_list:
    for group in element["sub_categories"]:
        print("그룹별 제품리스트를 추출합니다. : " + group["link"])
        group_product.append(product_list(link + "/category/" + group["link"]))
        time.sleep(2)

    all_product = []

    for i in group_product:
        for j in i:
            all_product.append(j)

    all_product = list(set(all_product))
    gender_types = []

    for a in all_product:
        gender_types.append(product_info(link + "/product/" + a))

    print(gender_types)


# this is for thumbnail for category and group
def for_thumbnail(target):
    driver.get(target)
    if driver.find_elements_by_xpath(
        "/html/body/section/main/section/div[1]/div[2]/div[1]/div[1]"
    ):
        print(
            driver.find_element_by_xpath(
                "/html/body/section/main/section/div[1]/div[2]/div[1]/div[1]"
            )
            .find_element_by_tag_name("img")
            .get_attribute("src")
        )


def product_list(target):
    scroll_down(target)
    # products = driver.find_elements_by_class_name("plp-grid-item")
    # product = products[0]
    product_list = [
        product.find_element_by_class_name("product-url")
        .get_attribute("href")
        .split("/")[-1]
        for product in driver.find_elements_by_class_name("plp-grid-item")
        if product.find_elements_by_class_name("product-url")
    ]
    time.sleep(2)
    return product_list


def product_info(target):
    driver.get(target)

    informations = driver.find_element_by_class_name("fixit-element.pdp-info")

    # 코드
    # target.split("/")[-1]

    # 이름
    # informations.find_element_by_class_name("product-name").text

    # 가격
    # informations.find_element_by_class_name("sale").get_attribute("data-price")

    # 고유색상
    # informations.find_element_by_class_name("value.over-txt").text

    # 성별타입
    # informations.find_element_by_class_name("product-badge,text-extrabold").text

    # 한줄설명
    # informations.find_element_by_class_name("product-description").text

    # 사이즈
    # [size.text for size in informations.find_elements_by_class_name("variation-size.selectable.input-radio")]

    # 한줄설명
    # [
    #     informations.find_element_by_class_name("product-description").text
    #     if informations.find_elements_by_class_name("product-description")
    #     else ""
    # ][0]

    print("제품에 대한 정보를 수집합니다." + target.split("/")[-1])

    print(a)
    return a


# tags
# pdp-details-content => d
# product-tags-contents => detail


initialize_db(link)

# print(os.getcwd())
# print(os.listdir())

driver.quit()
