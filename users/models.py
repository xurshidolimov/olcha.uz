from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class CustomUser(AbstractUser):
    phone_number = models.IntegerField(null=True, blank=True)
    money = models.IntegerField(default=0)

    def __str__(self):
        return self.username
