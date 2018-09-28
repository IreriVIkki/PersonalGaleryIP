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


class Image(models.Model, categories, Location):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=50)
    description = models.TextField()
    location = models.ForeignKey(Location)
    categories = models.ManyToManyField(categories, blank=True)
    posted_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    @classmethod
    def delete_by_id(cls, id):
        img = cls.objects.filter(pk=id)
        img.delete()

    @classmethod
    def all_photos(cls):
        return cls.objects.all()

    @classmethod
    def filter_by_categories(cls, search_cat):
        cat = categories.objects.filter(name=search_cat)
        return cls.objects.filter(categories=cat)

    @classmethod
    def filter_by_location(cls, search_loc):
        loc = Location.objects.filter(location=search_loc)
        return cls.objects.filter(location=loc)

    def __str__(self):
        return self.name
