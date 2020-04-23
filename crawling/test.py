import csv

# 실루엣, 컬러 구분
	# target = 'silhouette'
	# target = 'color'

	#with open(f'./data/{target}/{target}s.csv', newline='') as opened:
		#data_reader = csv.DictReader(opened)

		#newcsv = open(f"./data/{target}/{target}.csv", 'w+', encoding='utf-8')
		#csv.writer(newcsv).writerow(['pk',f'{target}_code'])

		#color_code_list=[0]
		#for row in data_reader:
		#	color_code_list.append(row[target])
		#colors = list(set(color_code_list))
		#for i in range(len(colors)-1):
		#	csv.writer(newcsv).writerow([i+1, colors[i+1]])
		#newcsv.close()

	#with open(f'./data/{target}/{target}s.csv', newline='') as opened:
		#data_reader = csv.DictReader(opened)

		#relcsv = open(f"./data/{target}/product_{target}.csv", 'w+', encoding='utf-8')
		#csv.writer(relcsv).writerow(['product_codes',f'{target}_code'])

		#for row in data_reader:
		#	csv.writer(relcsv).writerow([row['product_codes'], colors.index(f'{row[target]}')])
		#relcsv.close()

# 제품 테이블 병합
	#target = 'product'
	#combine = []

	# with open(f'./data/{target}/{target}_shoes.csv', newline='') as opened:# 
		#data_reader = csv.DictReader(opened)
		#for row in data_reader:
		#	combine.append([row['code'],row['name'],row['price'],row['gender'],row['size_list'],row['media_list'],row['info_long'],row['image_big']])

	# with open(f'./data/{target}/{target}_apparel-accessory.csv', newline='') as opened:
		# data_reader = csv.DictReader(opened)
		# for row in data_reader:
		# 	combine.append([row['code'],row['name'],row['price'],row['gender'],row['size_list'],row['media_list'],row['info_long'],row['image_big']])

	# with open(f'./data/{target}/{target}_kids-shoes.csv', newline='') as opened:
		# data_reader = csv.DictReader(opened)
		# for row in data_reader:
		# 	combine.append([row['code'],row['name'],row['price'],row['gender'],row['size_list'],row['media_list'],row['info_long'],row['image_big']])

	# combinedcsv = open(f"./data/{target}/{target}.csv", 'w+', encoding='utf-8')
	# csv.writer(combinedcsv).writerow(['code','name','price','gender','size_list','media_list','info_long','image_big'])
	# for row in combine:
		# csv.writer(combinedcsv).writerow(row)
	# combinedcsv.close()

# 설명 테이블 병합
	# target = 'description'
	# combine = []

	# with open(f'./data/{target}/{target}_shoes.csv', newline='') as opened:
		# data_reader = csv.DictReader(opened)
		# for row in data_reader:
		# 	combine.append([row['product_id'],row['description']])

	# with open(f'./data/{target}/{target}_apparel-accessory.csv', newline='') as opened:
		# data_reader = csv.DictReader(opened)
		# for row in data_reader:
		# 	combine.append([row['product_id'],row['description']])

	# with open(f'./data/{target}/{target}_kids-shoes.csv', newline='') as opened:
		# data_reader = csv.DictReader(opened)
		# for row in data_reader:
		# 	combine.append([row['product_id'],row['description']])

	# combinedcsv = open(f"./data/{target}/{target}.csv", 'w+', encoding='utf-8')
	# csv.writer(combinedcsv).writerow(['product_id','description'])
	# for row in combine:
		# csv.writer(combinedcsv).writerow(row)

	# combinedcsv.close()

# 카테고리 테이블 병합
	#target = 'category'
	#tlist = ['shoes', 'apparel-accessory', 'kids-shoes']
	#target = 'group'
	#tlist = [
	#'chucktaylorallstar', 'chuck70', 'onestar', 'jackpurcell',
	#'tops', 'pants', 'accessory',
	#'baby-shoes', 'kids']
	#combine = []
	
	#for name in tlist:
	#	with open(f'./data/{target}/{target}_{name}.csv', newline='') as opened:
	#		data_reader = csv.DictReader(opened)
	#		for row in data_reader:
	#			combine.append([row['product_id'],row[target]])
	#
	#combinedcsv = open(f"./data/{target}/product_{target}.csv", 'w+', encoding='utf-8')
	#csv.writer(combinedcsv).writerow(['product_id',target+'_id'])
	#for row in combine:
	#	csv.writer(combinedcsv).writerow(row)
	
	#combinedcsv.close()

