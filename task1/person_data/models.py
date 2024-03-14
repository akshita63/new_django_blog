from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    mobile_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    image_path = models.CharField(max_length=200, blank=True, null=True)
