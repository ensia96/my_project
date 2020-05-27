from django.db import models

class Comment(models.Model):
    name       = models.CharField(max_length = 50)
    content    = models.TextField()
    created    = models.DateTimeField(auto_now_add = True)
    updated    = models.DateTimeField(auto_now = True)