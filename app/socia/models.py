from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    interests = models.TextField(null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)


class CustomUser(UserProfile):
    class Meta:
        proxy = True
        ordering = ("first_name",)
