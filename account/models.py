from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    CHOICES = (('admin', 'Admin'), ('client', 'Client'), ('owner_arena', 'Owner Arena'))
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    role = models.CharField(choices=CHOICES, max_length=15, blank=True, null=True)
    complete = models.IntegerField(default=0)
    smscode = models.IntegerField(default=0)

    def __str__(self):
        return self.username
