from distutils.command.upload import upload
from django.db import models

# Create your models here.

class myservices(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to = 'pics')

class myskills(models.Model):
    name =  models.CharField(max_length=100)
    percent = models.IntegerField()

class myexperiences(models.Model):
    name = models.CharField(max_length=100)
    companyname= models.CharField(max_length=100)
    exp = models.CharField(max_length=100)
    img = models.ImageField(upload_to = 'pics')
    comment1 =  models.TextField()
    comment2 =  models.TextField()

class testimonials(models.Model):
    name= models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    comanyname= models.CharField(max_length=100)
    img= models.ImageField(upload_to = 'pics')
    comment = models.TextField()
