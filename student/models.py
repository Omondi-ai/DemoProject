from django.db import models
from welcome.models import CustomUser

class Articlee(models.Model):

    title = models.CharField(max_length =150)
    content = models.TextField(max_length = 10000)
    date_posted = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(CustomUser, max_length=10, on_delete=models.CASCADE, null=True)