from django.db import models

from service.models import SurveyResult, UserRoutine


class User(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=200)
    age = models.IntegerField()
    gender = models.CharField(max_length=5)
    survey = models.ManyToManyField("Survey", through="SurveyResult")
    routine = models.ManyToManyField("Routine", through="UserRoutine")

    class Meta:
        db_table = "users"
