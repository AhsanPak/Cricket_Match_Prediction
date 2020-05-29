from django.db import models
from django.utils import timezone
# Create your models here.

class cityy(models.Model):
    team = models.CharField(unique=True, max_length=255,)
    team1 = models.CharField(unique=True, max_length=255)
    city = models.CharField(unique=True, max_length=255)