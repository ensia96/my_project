from django.urls import path
from .views import Contents

urlpatterns = [
    path('', Contents.as_view()),
]