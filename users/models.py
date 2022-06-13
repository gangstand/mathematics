from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    group = models.CharField(null=True, blank=True, max_length=8)