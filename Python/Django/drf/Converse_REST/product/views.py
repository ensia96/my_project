from rest_framework import generics
from .models import *
from .serializers import *


class ListCatagoryView(generics.ListAPIView):

    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class ListProductView(generics.ListAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializers
