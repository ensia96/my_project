from rest_framework import serializers
from .models import *


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name")


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("code", "name", "price")
