from django.db import models


class Routine(models.Model):
    name = models.CharField(max_length=50)
    summary = models.CharField(max_length=100)
    exercise = models.ManyToManyField("Exercise", through="RoutineExercise")

    class Meta:
        db_table = "routines"


class RoutineExercise(models.Model):
    routine = models.ForeignKey("Routine", on_delete=models.CASCADE)
    exercies = models.ForeignKey("Exercise", on_delete=models.CASCADE)

    class Meta:
        db_table = "routines_exercises"


class Exercise(models.Model):
    name = models.CharField(max_length=50)
    tip = models.CharField(max_length=100)
    set = models.IntegerField()
    difficulty = models.ForeignKey("Difficulty", on_delete=models.SET_NULL, null=True)
    part = models.ForeignKey("Part", on_delete=models.SET_NULL, null=True)
    type = models.ForeignKey("Type", on_delete=models.SET_NULL, null=True)
    routine = models.ManyToManyField("Routine", through="RoutineExercise")

    class Meta:
        db_table = "exercises"


class Action(models.Model):
    content = models.CharField(max_length=500)
    exercise = models.ForeignKey("Exercise", on_delete=models.CASCADE)

    class Meta:
        db_table = "actions"


class Part(models.Model):
    content = models.CharField(max_length=30)

    class Meta:
        db_table = "parts"


class Difficulty(models.Model):
    content = models.CharField(max_length=10)

    class Meta:
        db_table = "difficulties"


class Type(models.Model):
    content = models.CharField(max_length=30)

    class Meta:
        db_table = "types"
