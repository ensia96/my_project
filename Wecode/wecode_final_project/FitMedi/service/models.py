from django.db import models

from user.models import User
from survey.models import Question, Answer
from exercise.models import Routine


class SurveyResult(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    question = models.ForeignKey("Question", on_delete=models.CASCADE)
    answer = models.ForeignKey("Answer", on_delete=models.CASCADE)

    class Meta:
        db_table = "users_surveys"


class UserRoutine(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    routine = models.ForeignKey("Routine", on_delete=models.CASCADE)

    class Meta:
        db_table = "users_routines"
