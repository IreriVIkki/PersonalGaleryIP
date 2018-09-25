from django.db import models

# Create your models here.


class Location(models.Model):
    location = models.CharField(max_length=30)

    def __str__(self):
        return self.location


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=50)
    description = models.TextField()
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)

    def __str__(self):
        return self.name
