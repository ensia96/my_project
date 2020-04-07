from django.urls import path, include

urlpatterns = [
    path('comment/', include('westagram.urls')),
]
