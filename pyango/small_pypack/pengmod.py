from django.db import models

class Booking(models.Model):

   time         = models.TimeField(auto_now=False, auto_now_add=False)
   name         = models.CharField(max_length=100)
   people       = models.IntegerField()
   info         = models.TextField()
   tel          = models.CharField(max_length=12)
   date         = models.DateField()
   initials     = models.CharField(max_length=20)
   created_date = models.DateTimeField(auto_now_add=True)
   table        = models.IntegerField(default=0)

   objects = models.Manager()

class Table(models.Model):

   table_num = models.IntegerField()
   people    = models.IntegerField()

   objects   = models.Manager()