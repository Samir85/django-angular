from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=255)
    last = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    adress = models.CharField( default=True ,max_length=255)
    zipcode =models.CharField(max_length=8)    

