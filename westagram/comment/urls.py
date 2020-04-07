from django.urls import path

from .views import Leave_comment

urlpatterns = [
    path('leave_comment', Leave_comment.as_view()),
]