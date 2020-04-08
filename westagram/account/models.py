from django.db import models

class Users(models.Model):
    name       = models.CharField(max_length = 50)
    password   = models.CharField(max_length = 300)
    created    = models.DateTimeField(auto_now_add = True)
    updated    = models.DateTimeField(auto_now = True)