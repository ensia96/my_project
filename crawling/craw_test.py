#상품정보 추출구문

    # gijun = 'shoes'
    # source=[
    # "https://www.converse.co.kr/category/"+gijun, # 스크롤 다운 주소
    # 'a', # list 요소의 정보 ( 태그 )
    # {'class':'product-url'}, # list 요소의 정보 ( 상세정보 )
    # 'href', # list 요소의 정보 ( 속성값 )
    # 'description_'+gijun, # CSV 파일 이름
    # ['product_id','description'], # 칼럼 뭉치
    # 'https://www.converse.co.kr/product/' # 반복 url root 주소
    # ]
    # needed={}
    # kvp={}
    # keyinput=[]
    # valueinput=[]
    # for ids in source[-1]:
    #     driver.get(source[6]+ids)
    #     for key in driver.find_elements_by_tag_name('dt'):
    #         if key.text != '':
    #             keyinput.append(key.text)
    #     for value in driver.find_elements_by_tag_name('dd'):
    #         if value.text != '':
    #             valueinput.append(value.text)
    #     for i in range(len(keyinput)):
    #         if keyinput[i] != '소비자피해 보증보험':
    #             kvp[keyinput[i]]=valueinput[i]
    #     needed[ids]=kvp
    #     print(f'제품 : {ids} ( {source[-1].index(ids)+1}/{len(source[-1])} )')
    #     kvp={}
    # print('정보 분류 완료')
    # for ids in source[-1]:
    #     csv.writer(newcsv).writerow([ids,needed[ids]])
    # newcsv.close()
    # driver.quit()

from craw import *

for_project()

#get_csv() # 실루엣, 컬러 연결관계