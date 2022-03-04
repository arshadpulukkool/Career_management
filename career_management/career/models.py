from django.db import models

# Create your models here.
class registration(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class login(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class courses(models.Model):
    cousename = models.CharField(max_length=50)
    duration = models.CharField(max_length=50)
    mode = models.CharField(max_length=50)
    institutename = models.CharField(max_length=100)
    location = models.CharField(max_length=100, default='')
    category = models.CharField(max_length=30)
    phone = models.CharField(max_length=20)
    details = models.CharField(max_length=999)
    rooms = models.CharField(max_length=999)


