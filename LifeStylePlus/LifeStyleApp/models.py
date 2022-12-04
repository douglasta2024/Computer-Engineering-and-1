from django.db import models

# Create your models here.
class Post(models.Model):
    days = models.IntegerField()
    miles = models.IntegerField()