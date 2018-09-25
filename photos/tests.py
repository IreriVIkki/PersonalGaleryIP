from django.test import TestCase
from .models import Image, Category, Location

# Create your tests here.


class GaleryTestCase(TestCase):


def setUp(self):
    self.nairobi = Location(locatio='Nairobi')
    self.nairobi.save()
    self.nature = Category(name='nature')
    self.nature.save()

    self.waterfall = Image(
        name='waterfall', description='picture of a waterfall')

    self.waterfall.category.add(self.nature)
    self.waterfall.location.add(self.nairobi)
    self.waterfall.save()
