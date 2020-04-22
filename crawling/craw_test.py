상품정보 추출구문
    needed={}
    kvp={}
    keyinput=[]
    valueinput=[]
    for ids in source[-1]:
        driver.get(source[6]+ids)
        for key in driver.find_elements_by_tag_name('dt'):
            if key.text != '':
                keyinput.append(key.text)
        for value in driver.find_elements_by_tag_name('dd'):
            if value.text != '':
                valueinput.append(value.text)
        for i in range(len(keyinput)):
            if keyinput[i] != '소비자피해 보증보험':
                kvp[keyinput[i]]=valueinput[i]
        needed[ids]=kvp
        print(f'정보단위 생성완료 / 제품id : {ids}')
        kvp={}
    print('정보 분류 완료')
    for ids in source[-1]:
        csv.writer(newcsv).writerow([ids,needed[ids]])
    newcsv.close()
    driver.quit()

aaa
    needed={}
    kvp={}
    keyinput=[]
    valueinput=[]
    for ids in source[-1]:
        driver.get(source[6]+ids)
        for key in driver.find_elements_by_tag_name('dt'):
            if key.text != '':
                keyinput.append(key.text)
        for value in driver.find_elements_by_tag_name('dd'):
            if value.text != '':
                valueinput.append(value.text)
        for i in range(len(keyinput)):
            if keyinput[i] != '소비자피해 보증보험':
                kvp[keyinput[i]]=valueinput[i]
        needed[ids]=kvp
        print(f'정보단위 생성완료 / 제품id : {ids}')
        kvp={}
    print('정보 분류 완료')
    for ids in source[-1]:
        csv.writer(newcsv).writerow([ids,needed[ids]])
    newcsv.close()
    driver.quit()