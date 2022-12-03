from django.db import models

# Create your models here.
class Post(models.Model):
    miles = models.IntegerField()
    minutes = models.IntegerField()