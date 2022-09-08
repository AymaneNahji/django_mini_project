from django.db import models


# Create your models here.

class User(models.Model):
    user_name = models.CharField(max_length=20,unique=True,null=False)
    password = models.CharField(max_length=20,null=False)

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.TextField()