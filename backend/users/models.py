from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date

# Create your models here.
class CustomUser(AbstractUser):
    birth_date = models.DateField(null=False, blank=False, default=date.today)

    def __str__(self):
        return self.username