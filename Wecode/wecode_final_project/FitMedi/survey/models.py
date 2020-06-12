from django.db import models

from exercise.models import Part


class Question(models.Model):
    content = models.CharField(max_length=100)

    class Meta:
        db_table = "questions"


class Answer(models.Model):
    content = models.CharField(max_length=100)
    part = models.ForeignKey("Part", on_delete=models.SET_NULL, null=True)
    question = models.ForeignKey("Question", on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = "answers"
