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
        self.wild = categories.objects.create(name='wild')

        self.waterfall = Image(
            name='waterfall', description='picture of a waterfall')

        self.waterfall.categoies.add(self.nature)
        self.waterfall.categoies.add(self.wild)
        self.waterfall.location.add(self.nairobi)
        self.waterfall.save()

    # def a testcase for instance of the waterfall class
    def test_image_instance(self):
        self.assertTrue(isinstance(self.waterfall, Image))

    def test_category_instance(self):
        self.assertTrue(isinstance(self.nature, categories))
        self.assertTrue(isinstance(self.wild, categories))

    def test_location_instance(self):
        self.assertTrue(isinstance(self.nairobi, Location))

    def test_delete_image(self):
        self.waterfall.delete()
        self.assertTrue(len(Image.objects.all()) == 0)

    def test_delete_by_id(self):
        Image.delete_by_id(self.waterfall.id)
        self.assertIsNone(self.waterfall, None)

    def test_categories(self):
        self.assertEqual(len(self.waterfall.categoies.all()), 2)
