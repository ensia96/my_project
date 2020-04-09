from django.urls import path
from .views import Create, Search

urlpatterns = [
    path('create', Create.as_view()),
    path('search', Search.as_view()),
]