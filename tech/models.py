from django.db import models

from django_ckeditor_5.fields import CKEditor5Field
from ckeditor.fields import RichTextField
# Create your models here.
from django.contrib.auth.models import User

# Create your models here.


class Blogs(models.Model):

    title = RichTextField()
    description = RichTextField()
    image = models.ImageField()
    date = models.DateField(auto_now_add=True)


class Services(models.Model):
    title = models.CharField(max_length=5000)
    description = RichTextField()
    image = models.ImageField()
    date = models.DateField(auto_now_add=True)


class Projets(models.Model):

    title = models.CharField(max_length=5000)
    description = models.TextField(max_length=2000)
    lien = models.CharField(max_length=500)
    image = models.ImageField()
    date = models.DateField(auto_now_add=True)


class Reviews(models.Model):
    customer = models.OneToOneField(User, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateField(auto_now_add=True)


class Pricings(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=5000)
    prise = models.IntegerField()
    pric1 = models.CharField(max_length=5000)
    pric2 = models.CharField(max_length=5000)
    pric3 = models.CharField(max_length=5000)
    pric4 = models.CharField(max_length=5000)
    pric5 = models.CharField(max_length=5000)
