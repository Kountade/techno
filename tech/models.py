from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.
from django.contrib.auth.models import User

# Create your models here.


class Blogs(models.Model):
    title = models.TextField()
    content = CKEditor5Field()
    image = models.ImageField()
    date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return self.title


class Services(models.Model):
    title = models.CharField(max_length=5000)
    description = CKEditor5Field()
    image = models.ImageField()
    date = models.DateField(auto_now_add=True)


class Projets(models.Model):

    title = models.CharField(max_length=5000)
    description = models.TextField(max_length=2000)
    lien = models.CharField(max_length=500)
    image = models.ImageField()
    date = models.DateField(auto_now_add=True)

class Equipe(models.Model):

    nom = models.CharField(max_length=5000)
    profession = models.TextField(max_length=2000)
    image = models.ImageField()
    date = models.DateField(auto_now_add=True)


class Entreprise(models.Model):

    name = models.CharField(max_length=5000)
    image = models.ImageField()
    date = models.DateField(auto_now_add=True)


class Reviews(models.Model):
    nom  = models.TextField(max_length=100)
    text = models.TextField()
    image = models.ImageField()
    date = models.DateField(auto_now_add=True)


class Pricings(models.Model):
    # Classe FontAwesome pour les icônes
    icon_class = models.CharField(max_length=255)
    title = models.CharField(max_length=5000)
    prise = models.IntegerField()
    pric1 = models.CharField(max_length=5000)
    pric2 = models.CharField(max_length=5000)
    pric3 = models.CharField(max_length=5000)
    pric4 = models.CharField(max_length=5000)
    pric5 = models.CharField(max_length=5000)

    def __str__(self):
        return self.title
