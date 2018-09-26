from django.db import models

# Create your models here.


class Location(models.Model):
    location = models.CharField(max_length=30)

    def __str__(self):
        return self.location


class categories(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=50)
    description = models.TextField()
    location = models.ForeignKey(Location)
    categoies = models.ManyToManyField(categories)

    class Meta:
        ordering = ['name']

    @classmethod
    def delete_by_id(cls, id):
        img = cls.objects.filter(pk=id)
        img.delete()

    def __str__(self):
        return self.name
