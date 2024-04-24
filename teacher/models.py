from django.db import models
from welcome.models import CustomUser
from django.utils import timezone


class Teacher(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=20)


class Article(models.Model):
    title = models.CharField(max_length =150)
    content = models.TextField(max_length = 10000)
    date_posted = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(CustomUser, max_length=10, on_delete=models.CASCADE, null=True)
