from django.db import models

class Category(models.Model): # 음료, 푸드 등 카테고리 ( 대분류 ) 에 대한 분류를 위한 카테고리테이블
    name        = models.CharField(max_length=20)

class Group(models.Model): # 콜드브루, 브루드커피 등 제품군 ( 중분류 ) 에 대한 분류가 이루어지는 제품군테이블
    name        = models.CharField(max_length=20)
    category_id = models.ForeignKey(Category, on_delete = models.CASCADE)

class Product(models.Model): # 관리할 핵심데이터인 각종 제품들 ( 세분류 ) 에 대한 분류가 이루어지는 제품테이블
    name_ko     = models.CharField(max_length=50)
    name_en     = models.CharField(max_length=50)
    group_id    = models.ForeignKey(Group, on_delete = models.CASCADE)

class Allergy(models.Model): # 1 제품당, 0 ~ 알레르기
    name        = models.CharField(max_length=20)
    products    = models.ManytoManyField(Product)

class Description(models.Model): # 1 제품당, 0 ~ 설명
    description = models.TextField(blank=True)
    products    = models.ManytoManyField(Product)

class Ingredient(models.Model): # 1 제품당, 1 영양정보
    size_id     = models.CharField(max_length=20)
    kcal        = models.FloatField()
    sugar       = models.FloatField()
    protein     = models.FloatField()
    sodium      = models.FloatField()
    fat         = models.FloatField()
    caffeine    = models.FloatField()
    product_id  = models.ForeignKey(Product, on_delete = models.CASCADE)

class Size(models.Model): # 1 영양정보당, 1 사이즈 ( 기준용량 )
    name        = models.CharField(max_length=20)
    num_ml      = models.IntegerField()
    num_oz      = models.IntegerField()