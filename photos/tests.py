from django.test import TestCase
from .models import Image, categories, Location

# Create your tests here.


class GaleryTestCase(TestCase):

    # def class instance setup for the project
    def setUp(self):
        self.nairobi = Location(location='Nairobi')
        self.nairobi.save()
        self.nature = categories(name='nature')
        self.nature.save()

        self.waterfall = Image(
            name='waterfall', description='picture of a waterfall')

        self.waterfall.categoies.add(self.nature)
        self.waterfall.location.add(self.nairobi)
        self.waterfall.save()

    # def a testcase for instance of the waterfall class
    def test_image_instance(self):
        self.assertTrue(isinstance(self.waterfall, Image))
