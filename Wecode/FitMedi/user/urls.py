from django.urls import path
from user.views import UserAuthView

urlpatterns = [
    path("auth", UserAuthView.as_view()),
]
