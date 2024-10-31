from django.db import models

# Create your models here.
class Countries(models.Model):
    code = models.CharField(max_length=3)
    flag = models.CharField(max_length=100)
