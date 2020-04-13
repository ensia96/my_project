from django.db import models

class Category(models.Model): # 음료, 푸드 등 카테고리 ( 대분류 ) 에 대한 분류를 위한 카테고리테이블
    name            = models.CharField(max_length=20)

    class Meta:
        db_table = 'category'

class Group(models.Model): # 콜드브루, 브루드커피 등 제품군 ( 중분류 ) 에 대한 분류가 이루어지는 제품군테이블
    name            = models.CharField(max_length=20)
    category        = models.ForeignKey('Category', on_delete = models.SET_NULL, null=True)

    class Meta:
        db_table = 'group'

class Product(models.Model): # 관리할 핵심데이터인 각종 제품들 ( 세분류 ) 에 대한 분류가 이루어지는 제품테이블
    name_ko         = models.CharField(max_length=50)
    name_en         = models.CharField(max_length=50)
    category        = models.ForeignKey('Category', on_delete = models.SET_NULL, null=True)
    group           = models.ForeignKey(Group, on_delete = models.SET_NULL, null=True)

    class Meta:
        db_table = 'product'


class Image(models.Model): # 이미지 주소 테이블
    img_url         = models.URLField(max_length=2000)
    product         = models.ForeignKey('Product', on_delete = models.SET_NULL, null=True)

    class Meta:
        db_table = 'image'

class Product_Allergy(models.Model): # 제품 - 알레르기 연결	
    product         = models.ForeignKey('Product', on_delete = models.SET_NULL, null=True)
    allergy         = models.ForeignKey('Allergy', on_delete = models.SET_NULL, null=True)

    class Meta:
        db_table = 'product_allergy'

class Allergy(models.Model): # 1 제품당, 0 ~ 알레르기
    name            = models.CharField(max_length=20)
    product         = models.ManyToManyField('Product', through=Product_Allergy)

    class Meta:
        db_table = 'allergy'

class Product_Description(models.Model): # 제품 - 설명 연결	
    product         = models.ForeignKey('Product', on_delete = models.SET_NULL, null=True)
    description     = models.ForeignKey('Description', on_delete = models.SET_NULL, null=True)

    class Meta:
        db_table = 'product_description'

class Description(models.Model): # 1 제품당, 0 ~ 설명
    description     = models.CharField(max_length=300)
    product         = models.ManyToManyField('Product', through=Product_Description)

    class Meta:
        db_table = 'description'

class Ingredient(models.Model): # 1 제품당, 1 영양정보
    size            = models.CharField(max_length=20)
    kcal            = models.DecimalField(max_digits=5, decimal_places=2)
    sugar           = models.DecimalField(max_digits=5, decimal_places=2)
    protein         = models.DecimalField(max_digits=5, decimal_places=2)
    sodium          = models.DecimalField(max_digits=5, decimal_places=2)
    fat             = models.DecimalField(max_digits=5, decimal_places=2)
    caffeine        = models.DecimalField(max_digits=5, decimal_places=2)
    product         = models.ForeignKey(Product, on_delete = models.SET_NULL, null=True)

    class Meta:
        db_table = 'ingredient'

class Size(models.Model): # 1 영양정보당, 1 사이즈 ( 기준용량 )
    name            = models.CharField(max_length=20)
    num_ml          = models.IntegerField()
    num_oz          = models.IntegerField()

    class Meta:
        db_table = 'size'