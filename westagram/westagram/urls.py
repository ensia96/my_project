from django.urls import path, include

urlpatterns = [
    path('comment/', include('comment.urls')),
    path('userauth/', include('userauth.urls')),
]