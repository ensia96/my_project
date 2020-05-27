from django.urls import path
from .views import UserView, UserAuthView

urlpatterns = [
    path('/sign-up', UserView.as_view()),
    path('/sign-in', UserAuthView.as_view()),
]
#UserDetailView