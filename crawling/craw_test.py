# 상품정보 추출구문
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
    #         if keyinput[i] != '소비자피해 보증보험' and keyinput[i] != 'Model':
    #             if keyinput[i] != 'Model':
    #                 kvp[keyinput[i]]=valueinput[i]
    #     needed[ids]=kvp
    #     print(f'제품 : {ids} ( {source[-1].index(ids)+1}/{len(source[-1])} )')
    #     kvp={}
    # print('정보 분류 완료')
    # for ids in source[-1]:
    #     csv.writer(newcsv).writerow([ids,needed[ids]])
    # newcsv.close()
    # driver.quit()

# 카테고리 / 그룹
    # 신발 1 / 의류 2 / 아동 3
        # 척테일러 1 / 척70 2 / 원스타 3 / 잭퍼셀 4
        # 상의 5 / 하의 6 / 악세서리 7
        # 유아 8 / 어린이 9
    #    taarget = 'group'
    #    gijun = 'kids'
    #    pk=9
    #    source=[
    #    "https://www.converse.co.kr/category/"+gijun,
    #    'a',
    #    {'class':'product-url'},
    #    'href',
    #    taarget+'_'+gijun,
    #    ['product_id',taarget],
    #    'https://www.converse.co.kr/product/'
    #    ]
    #    for ids in source[-1]:
    #        csv.writer(newcsv).writerow([ids,1])
    #        print(f'제품 : {ids} ( {source[-1].index(ids)+1}/{len(source[-1])} )')
    #    print('정보 분류 완료')
    #    newcsv.close()
    #    driver.quit()

# 실루엣, 컬러 구분
    #import csv
    #target = 'color' # 'silhouette'
    #
    #with open(f'./data/{target}/{target}s.csv', newline='') as opened:
    #	data_reader = csv.DictReader(opened)
    #
    #	newcsv = open(f"./data/{target}/{target}.csv", 'w+', encoding='utf-8')
    #	csv.writer(newcsv).writerow(['pk',f'{target}_code'])
    #
    #	colors=[0,'000000','0000FF','009900','131936','6600CC','996633','999999','A39264','F0E4D2','FF0000','FF6600','FFB6C1','FFCC00','FFFFFF']
    #	for i in range(len(colors)-1):
    #		csv.writer(newcsv).writerow([i+1, colors[i+1]])
    #	newcsv.close()
    #
    #with open(f'./data/{target}/{target}s.csv', newline='') as opened:
    #	data_reader = csv.DictReader(opened)
    #
    #	relcsv = open(f"./data/{target}/product_{target}.csv", 'w+', encoding='utf-8')
    #	csv.writer(relcsv).writerow(['product_codes',f'{target}_code'])
    #
    #	for row in data_reader:
    #		csv.writer(relcsv).writerow([row['product_codes'], colors.index(f'{row[target]}')])
    #	relcsv.close()

# 제품 테이블 병합
    # import csv
    # target = 'product'
    # combine = []
    # with open(f'./data/{target}/{target}_shoes.csv', newline='') as opened:# 
    # 	data_reader = csv.DictReader(opened)
    # 	for row in data_reader:
    # 		combine.append([row['code'],row['name'],row['price'],row['gender'],row['size_list'],row['media_list'],row['info_long'],row['image_big']])
    # 
    # with open(f'./data/{target}/{target}_apparel-accessory.csv', newline='') as opened:
    # 	data_reader = csv.DictReader(opened)
    # 	for row in data_reader:
    # 		combine.append([row['code'],row['name'],row['price'],row['gender'],row['size_list'],row['media_list'],row['info_long'],row['image_big']])
    # 
    # with open(f'./data/{target}/{target}_kids-shoes.csv', newline='') as opened:
    # 	data_reader = csv.DictReader(opened)
    # 	for row in data_reader:
    # 		combine.append([row['code'],row['name'],row['price'],row['gender'],row['size_list'],row['media_list'],row['info_long'],row['image_big']])
    # 
    # combinedcsv = open(f"./data/{target}/{target}.csv", 'w+', encoding='utf-8')
    # csv.writer(combinedcsv).writerow(['code','name','price','gender','size_list','media_list','info_long','image_big'])
    # 
    # for row in combine:
    # 	csv.writer(combinedcsv).writerow(row)
    # combinedcsv.close()

# 설명 테이블 병합
    #import csv
    #target = 'description'
    #combine = []
    #
    #with open(f'./data/{target}/{target}_shoes.csv', newline='') as opened:
    #	data_reader = csv.DictReader(opened)
    #	for row in data_reader:
    #		combine.append([row['product_id'],row['description']])
    #
    #with open(f'./data/{target}/{target}_apparel-accessory.csv', newline='') as opened:
    #	data_reader = csv.DictReader(opened)
    #	for row in data_reader:
    #		combine.append([row['product_id'],row['description']])
    #
    #with open(f'./data/{target}/{target}_kids-shoes.csv', newline='') as opened:
    #	data_reader = csv.DictReader(opened)
    #	for row in data_reader:
    #		combine.append([row['product_id'],row['description']])
    #
    #combinedcsv = open(f"./data/{target}/{target}.csv", 'w+', encoding='utf-8')
    #csv.writer(combinedcsv).writerow(['product_id','description'])
    #
    #for row in combine:
    #	csv.writer(combinedcsv).writerow(row)
    #combinedcsv.close()

# 카테고리 테이블 병합
	#import csv
	#target = 'category'
	#tlist = ['shoes', 'apparel-accessory', 'kids-shoes']
	#combine = []
	#	
	#for name in tlist:
	#	with open(f'./data/{target}/{target}_{name}.csv', newline='') as opened:
	#		data_reader = csv.DictReader(opened)
	#		for row in data_reader:
	#			combine.append([row['product_id'],row[target]])
	#
	#combinedcsv = open(f"./data/{target}/product_{target}.csv", 'w+', encoding='utf-8')
	#csv.writer(combinedcsv).writerow(['product_id',target+'_id'])
	#
	#for row in combine:
	#	csv.writer(combinedcsv).writerow(row)
	#	
	#combinedcsv.close()

# 그룹 테이블 병합
    #import csv
    #target = 'group'
    #tlist = [
    #'chucktaylorallstar', 'chuck70', 'onestar', 'jackpurcell',
    #'tops', 'pants', 'accessory',
    #'baby-shoes', 'kids']
    #combine = []
    #	
    #for name in tlist:
    #	with open(f'./data/{target}/{target}_{name}.csv', newline='') as opened:
    #		data_reader = csv.DictReader(opened)
    #		for row in data_reader:
    #			combine.append([row['product_id'],row[target]])
    #
    #combinedcsv = open(f"./data/{target}/product_{target}.csv", 'w+', encoding='utf-8')
    #csv.writer(combinedcsv).writerow(['product_id',target+'_id'])
    #
    #for row in combine:
    #	csv.writer(combinedcsv).writerow(row)
    #	
    #combinedcsv.close()

# 사이즈 테이블 병합
    #import csv
    #target = 'size'
    #taarget = ['shoes','apparel-accessory','kids-shoes']
    #combine = []
    #
    #for tar in taarget:
    #    with open(f'./data/{target}/{target}_shoes.csv', newline='') as opened:
    #    	data_reader = csv.DictReader(opened)
    #    	for row in data_reader:
    #    		combine.append([row['code'],row[target+'_list']])
    #
    #combinedcsv = open(f"./data/{target}/{target}.csv", 'w+', encoding='utf-8')
    #csv.writer(combinedcsv).writerow(['code',target])
    #
    #for row in combine:
    #	csv.writer(combinedcsv).writerow(row)
    #combinedcsv.close()

# 사이즈 구분
    #import csv
    #target = 'size'
    #
    #with open(f'./data/{target}/{target}s.csv', newline='') as opened:
    #    data_reader = csv.DictReader(opened)
    #    newcsv = open(f"./data/{target}/{target}.csv", 'w+', encoding='utf-8')
    #    csv.writer(newcsv).writerow(['pk',f'{target}'])
    #    size_list=[]
    #    for row in data_reader:
    #        size_list.append(row[target])
    #    size_list = set(size_list)
    #    size_list.remove('FREE')
    #    size_list.remove('Free Size')
    #    size_list = list(size_list)
    #    for i in size_list:
    #        size_list[size_list.index(i)] = int(i)
    #    size_list.sort()
    #    size_list.append('FREE')
    #    size_list.append('Free Size')
    #    sizes = size_list
    #    for i in size_list:
    #        sizes[size_list.index(i)] = str(i)
    #    for i in range(len(sizes)-1):
    #        csv.writer(newcsv).writerow([i+1, sizes[i+1]])
    #    newcsv.close()
    #
    #with open(f'./data/{target}/{target}s.csv', newline='') as opened:
    #	data_reader = csv.DictReader(opened)
    #
    #	relcsv = open(f"./data/{target}/product_{target}.csv", 'w+', encoding='utf-8')
    #	csv.writer(relcsv).writerow(['product_code',f'{target}_id'])
    #
    #	for row in data_reader:
    #		csv.writer(relcsv).writerow([row['code'], sizes.index(f'{row[target]}')])
    #	relcsv.close()

# 컨버스 나뉜파일 합치기
    #import csv
    #target = 'converse'
    #tlist = ['shoes', 'clothes', 'kids']
    #combine = []
    #	
    #for name in tlist:
    #    with open(f'./data/{target}_{name}.csv', newline='') as opened:
    #        data_reader = csv.DictReader(opened)
    #        for row in data_reader:
    #            if name == 'shoes':
    #                combine.append([row['code'],row['name'],row['price'],row['gender'],row['summary'],row['color_name'],row['series_list'],row['series_img_list'],row['size_list'],row['media_list'],row['info_long'],'',row['image_big'],row['information']])
    #            else:
    #                combine.append([row['code'],row['name'],row['price'],row['gender'],row['summary'],row['color_name'],row['series_list'],row['series_img_list'],row['size_list'],row['media_list'],row['info_long'],row['size_img'],row['image_big'],row['information']])
    #
    #combinedcsv = open(f"./data/product.csv", 'w+', encoding='utf-8')
    #csv.writer(combinedcsv).writerow(['code','name','price','gender','summary','color_name','series_list','series_img_list','size_list','media_list','info_long','size_img','image_big','information'])
    #
    #for row in combine:
    #	csv.writer(combinedcsv).writerow(row)
    #	
    #combinedcsv.close()


#from craw import *
#for_project()

#from crawling import *
#get_csv()
#get_product_data('size')

