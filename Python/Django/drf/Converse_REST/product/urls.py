from django.urls import path
from .views import *

urlpatterns = [
    path("/cat", ListCatagoryView.as_view(), name="category"),
    path("", ListProductView.as_view(), name="product"),
]
