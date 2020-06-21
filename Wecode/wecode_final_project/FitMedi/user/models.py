from django.db import models


class User(models.Model):
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=20)
    age = models.IntegerField()
    gender = models.CharField(max_length=5)
    routine = models.ManyToManyField("exercise.Routine", through="UserRoutine")

    class Meta:
        db_table = "users"


class SurveyResult(models.Model):
    user = models.ForeignKey("User", on_delete=models.SET_NULL, null=True)
    question = models.ForeignKey(
        "survey.Question", on_delete=models.SET_NULL, null=True
    )
    answer = models.ForeignKey("survey.Answer", on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = "users_surveys"


class UserRoutine(models.Model):
    user = models.ForeignKey("User", on_delete=models.SET_NULL, null=True)
    routine = models.ForeignKey(
        "exercise.Routine", on_delete=models.SET_NULL, null=True
    )

    class Meta:
        db_table = "users_routines"
