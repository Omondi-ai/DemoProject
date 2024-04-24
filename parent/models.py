from django.db import models

from welcome.models import CustomUser

class Parent(models.Model):

    parent_name = models.CharField(max_length=300)
    is_active = models.BooleanField(default=True)

    user = models.OneToOneField(CustomUser,max_length=10, on_delete=models.CASCADE, unique=True)

    def __str__(self):
        return f'{self.parent_name}  can now view'

        
