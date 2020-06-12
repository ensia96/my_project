from django.db import models
from base.models import Media


class Category(models.Model):
    name = models.CharField(max_length=30)
    link = models.CharField(max_length=30)
    thumbnail = models.ForeignKey("Media", on_delete=models.SET_NULL, null=True)
    super = models.ForeignKey("self", on_delete=models.CASCADE)
    product = models.ManyToManyField(
        "Product", through="CategoryProduct", through_fields=("category", "product")
    )

    class Meta:
        db_table = "categories"


class CategoryProduct(models.Model):
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey("Product", on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = "categories_products"


class Series(models.Model):
    number = models.CharField(max_length=30)
    product = models.ForeignKey("Product", on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = "series"


class Product(models.Model):
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    colour = models.CharField(max_length=30)
    summary = models.CharField(max_length=200)
    card = models.ForeignKey("Media", on_delete=models.SET_NULL, null=True)
    hover = models.ForeignKey("Media", on_delete=models.SET_NULL, null=True)
    type = models.ForeignKey("Type", on_delete=models.SET_NULL, null=True)
    target = models.ForeignKey("Target", on_delete=models.SET_NULL, null=True)
    detail = models.ForeignKey("Detail", on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = "products"


class Description(models.Model):
    content = models.CharField(max_length=100)
    product = models.ForeignKey("Product", on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = "descriptions"


class Type(models.Model):
    content = models.CharField(max_length=50)

    class Meta:
        db_table = "types"


class Target(models.Model):
    content = models.CharField(max_length=50)

    class Meta:
        db_table = "targets"


class Detail(models.Model):
    key = models.ForeignKey("DetailKey", on_delete=models.SET_NULL, null=True)
    value = models.ForeignKey("DetailValue", on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = "details"


class DetailKey(models.Model):
    content = models.CharField(max_length=50)

    class Meta:
        db_table = "detail_keys"


class DetailValue(models.Model):
    content = models.CharField(max_length=50)

    class Meta:
        db_table = "detail_values"


class ProductColor(models.Model):
    product = models.ForeignKey("Product", on_delete=models.SET_NULL, null=True)
    color = models.ForeignKey("Color", on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = "products_colors"


class Color(models.Model):
    content = models.CharField(max_length=50)

    class Meta:
        db_table = "colors"


class ProductSize(models.Model):
    product = models.ForeignKey("Product", on_delete=models.SET_NULL, null=True)
    size = models.ForeignKey("Size", on_delete=models.SET_NULL, null=True)
    amount = models.IntegerField()

    class Meta:
        db_table = "products_sizes"


class Size(models.Model):
    content = models.CharField(max_length=50)

    class Meta:
        db_table = "sizes"


class ProductMedia(models.Model):
    product = models.ForeignKey("Product", on_delete=models.SET_NULL, null=True)
    media = models.ForeignKey("Media", on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = "products_medias"
