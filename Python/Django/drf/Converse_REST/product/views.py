from rest_framework import generics
from rest_framework.decorators import api_view
from .models import *
from .serializers import *


class ListCatagoryView(generics.ListAPIView):

    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class ListProductView(generics.ListAPIView):

    queryset = Product.objects.all()
    # get_queryset()
    serializer_class = ProductSerializers
    # get_serializer_class()


class ProductView(generics.RetrieveAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializers


class CategoryView(generics.GenericAPIView):
    lookup_url_kwarg = ["gender", "color", "size", "silhouette"]
    lookup_field = "haha"

    queryset = Product.objects.all()


# @api_view()
# def mainview(request):
#     return Response({'some':'res'})
