from django.urls import path

from .views import Sign_up, Sign_in

urlpatterns = [
    path('sign_up', Sign_up.as_view()),
    path('sign_in', Sign_in.as_view()),
]