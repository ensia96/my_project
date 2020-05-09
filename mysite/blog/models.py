from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    user_nick = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.updated = timezone.now()
        self.save()

    def __str__(self):
        return self.title