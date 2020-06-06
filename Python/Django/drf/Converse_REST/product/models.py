from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30)
    link = models.CharField(max_length=30)
    thumbnail = models.ForeignKey('Media', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = "categories"


class Group(models.Model):
    name = models.CharField(max_length=40)
    link = models.CharField(max_length=40)
    thumbnail = models.ForeignKey('Media', on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = "groups"


class Series(models.Model):
    name = models.CharField(max_length=30)
    summary = models.CharField(max_length=100)

    class Meta:
        db_table = "series"


class Product(models.Model):
    code = models.CharField(max_length=45)
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    colour = models.CharField(max_length=45)
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True)
    group = models.ForeignKey("Group", on_delete=models.SET_NULL, null=True)
    series = models.ForeignKey("Series", on_delete=models.SET_NULL, null=True)
    card = models.ForeignKey("Media", on_delete=models.SET_NULL, null=True)
    hover = models.ForeignKey("Media", on_delete=models.SET_NULL, null=True)
    type = models.ForeignKey("Type", on_delete=models.SET_NULL, null=True)
    target = models.ForeignKey("Target", on_delete=models.SET_NULL, null=True)
    detail = models.ForeignKey('Detail', on_delete=models.SET_NULL, null=True)
    product_size = models.ManyToManyField("Size", through="ProductSize")
    product_color = models.ManyToManyField("Color", through="ProductColor")
    product_media = models.ManyToManyField("Media", through="ProductColor")

    class Meta:
        db_table = "products"


class Detail(models.Model):
    key = models.CharField(max_length=500)
    value = models.CharField(max_length=500)

    class Meta:
        db_table = "details"


class Description(models.Model):
    content = models.CharField(max_length=500, null=True)
    product = models.ForeignKey("Product", on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = "descriptions"


class Media(models.Model):
    media_url = models.URLField(max_length=2000)

    class Meta:
        db_table = "medias"


class Type(models.Model):
    name = models.CharField(max_length=10)

    class Meta:
        db_table = "types"


class Target(models.Model):
    name = models.CharField(max_length=10)

    class Meta:
        db_table = "targets"


class Color(models.Model):
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=50)

    class Meta:
        db_table = "colors"


class Size(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "sizes"


class ProductColor(models.Model):
    product = models.ForeignKey("Product", on_delete=models.SET_NULL, null=True)
    color = models.ForeignKey("Color", on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = "products_colors"


class ProductSize(models.Model):
    product = models.ForeignKey("Product", on_delete=models.SET_NULL, null=True)
    size = models.ForeignKey("Size", on_delete=models.SET_NULL, null=True)
    amount = models.IntegerField()

    class Meta:
        db_table = "products_sizes"


class ProductMedia(models.Model):
    product = models.ForeignKey("Product", on_delete=models.SET_NULL, null=True)
    media = models.ForeignKey("Media", on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = "products_medias"