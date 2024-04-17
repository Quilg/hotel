from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()

    def __str__(self) -> str:
        return self.name
    

class Sanatorium(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name
