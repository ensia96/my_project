from django.db import models


class Media(models.Model):
    url = models.CharField(max_length=2000)

    class Meta:
        db_table = "medias"
