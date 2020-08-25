from django.db import models
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
    age = models.IntegerField(blank=True, null=True)
    displayname = models.CharField(max_length=240, default="")
    homepage = models.URLField(blank=True, null=True)