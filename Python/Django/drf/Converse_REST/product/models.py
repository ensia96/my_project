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
    name = 