from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User


class User(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    TOKEN = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.user

    class Meta:
        db_table = 'User'
