from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30)
    link = models.CharField(max_length=30)
    thumbnail = models.ForeignKey("Media", on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = "categories"


class Group(models.Model):
    name = models.CharField(max_length=30)
    link = models.CharField(max_length=30)
    thumbnail = models.ForeignKey("Media", on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = "categories"


class Series(models.Model):
    name = models.CharField(max_length=30)
    summary = models.CharField(max_length=30)

    class Meta:
        db_table = "series"


class Product(models.Model):
    code = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    colour = models.CharField(max_length=30)
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True)
    group = models.ForeignKey("Group", on_delete=models.SET_NULL, null=True)
    series = models.ForeignKey("Series", on_delete=models.SET_NULL, null=True)
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
