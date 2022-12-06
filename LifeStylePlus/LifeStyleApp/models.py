from django.db import models

# Create your models here.
class Post(models.Model): #Model created to help take user input
    days = models.IntegerField()
    miles = models.IntegerField()