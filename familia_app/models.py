from django.db import models

# Create your models here.

class Familia(models.Model):
    name = models.CharField(max_length=100)
    dni = models.IntegerField()
    fecha = models.CharField(max_length=10)

