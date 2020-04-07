from django.db import models

class Account(models.Model):
    name       = models.CharField(max_length = 50)
    password   = models.CharField(max_length = 400)
    created    = models.DateTimeField(auto_now_add = True)
    updated    = models.DateTimeField(auto_now = True)