from django.test import TestCase
from .models import Image, categories, Location

# Create your tests here.


class GaleryTestCase(TestCase):

    # def class instance setup for the project
    def setUp(self):
        self.nairobi = Location.objects.create(location='Nairobi')
        self.nature = categories.objects.create(name='nature')
        self.wild = categories.objects.create(name='wild')

        self.waterfall = Image(
            name='waterfall', description='picture of a waterfall')

        self.waterfall.categoies.add(self.nature)
        self.waterfall.categoies.add(self.wild)
        self.waterfall.location.add(self.nairobi)

    # def a testcase for instance of the waterfall class
    def test_image_instance(self):
        self.waterfall.save()
        self.assertTrue(isinstance(self.waterfall, Image))

    def test_category_instance(self):
        self.waterfall.save()
        self.assertTrue(isinstance(self.wild, categories))
        self.assertTrue(isinstance(self.nature, categories))

    def test_location_instance(self):
        self.waterfall.save()
        self.assertTrue(isinstance(self.nairobi, Location))

    def test_delete_image(self):
        self.waterfall.save()
        self.waterfall.delete()
        self.assertTrue(len(Image.objects.all()) == 0)

    def test_delete_by_id(self):
        self.waterfall.save()
        Image.delete_by_id(self.waterfall.id)
        self.assertIsNone(self.waterfall, None)

        self.waterfall.save()
        self.assertEqual(len(self.waterfall.categoies.all()), 4)
