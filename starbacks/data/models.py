from django.db import models

class Category(models.Model): # 음료, 푸드 등 카테고리 ( 대분류 ) 에 대한 분류를 위한 카테고리테이블
    name=models.CharField(max_length=20)

# 카테고리 항목 1개당 제품군 여러가지

class Group(models.Model): # 콜드브루, 브루드커피 등 제품군 ( 중분류 ) 에 대한 분류가 이루어지는 제품군테이블
    name=models.CharField(max_length=20)

# 제품군 항목 1개당 제품 여러가지

class Product(models.Model): # 각종 메뉴들 ( 관리 데이터 단위 ) 에 대한 분류가 이루어지는 제품테이블
    name_ko=models.CharField(max_length=50)
    name_en=models.CharField(max_length=50)



# 1 제품당 0 ~ 여러 알레르기

class Allergy(models.Model): # 알레르기 품목 나열
    name=models.CharField(max_length=20)



class Description(models.Model): # 제품 1개당 상세설명 1 row
    desc_top=models.TextField()
    desc_btm=models.TextField()



class Ingredient(models.Model): # 제품 1개당 영양정보 1 row
    name=models.CharField(max_length=20)


class Ammount(models.Model): # 영양정보 1개당 기준량 1 row
    name=models.CharField(max_length=20)
    num=models.IntegerField


# models.ForeignKey(클래스, on_delete = models.CASCADE)