from django.db import models
from . managers import CustomUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = None
    email = models.EmailField(unique = True)
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=55)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    is_teacher = models.BooleanField(default=False, verbose_name="Are you a teacher?")
    is_student = models.BooleanField(default=False, verbose_name="Are you a student")
    is_parent = models.BooleanField(default=False,verbose_name='Are you a parent')


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return self.email

