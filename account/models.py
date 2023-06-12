from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    complete = models.IntegerField(default=0)
    smscode = models.IntegerField(default=0)

    def __str__(self):
        return self.username
