from selenium import webdriver
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
# 혹은 options.add_argument("--disable-gpu")

driver = webdriver.Chrome('/Users/ensia96/Documents/chromedriver', options=options)

driver.implicitly_wait(1)

driver.get('https://www.starbucks.co.kr/menu/drink_list.do') # starbuck url 접근
bs = BeautifulSoup(driver.page_source, 'html.parser')


# 음료 카테고리의 제품군
# under_category = bs.findAll('label',{'for':re.compile('product_*')})
# 
# for group in under_category:
#     group_name = group.text
#     print(group_name)

#wtf = bs.findAll('tbody')

# 제품명, 영양정보 다 얻어옴 => ' 7로 나눈 나머지가 1 -> 제품명 / 다른경우는 다 영양정보 ' 로 분류 가능

wtf = bs.findAll('td')

product = []
ingredient = []
i = 0
while i < len(wtf):
    omg = wtf[i].text
    if (i % 7) == 0:
        product.append(omg)
    i += 1
print(f"product = {product}")


driver.quit() # 안닫아주면 계속 창생겨서 렉걸림;