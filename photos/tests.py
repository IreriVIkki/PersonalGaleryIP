from django.test import TestCase
from .models import Image, categories, Location


#  test categories class
class TestCategories (TestCase):
    def setUp(self):
        self.nature = categories(name='nature')

    def test_instance(self):
        self.nature.save()
        self.assertTrue(isinstance(self.nature, categories))


#  test Location class
class TestLocation (TestCase):
    def setUp(self):
        self.nairobi = Location(location='Nairobi')

    def test_instance(self):
        self.nairobi.save()
        self.assertTrue(isinstance(self.nairobi, Location))


class ImageTest(TestCase):

    # def class instance setup for the project
    def setUp(self):
        self.nairobi = Location.objects.create(location='Nairobi')
        self.nature = categories.objects.create(name='nature')
        self.wild = categories.objects.create(name='wild')

        self.waterfall = Image.objects.create(
            name='waterfall', location=self.nairobi,  description='picture of a waterfall')

        self.waterfall.categories.add(self.nature)
        self.waterfall.categories.add(self.wild)

    # def a testcase for instance of the waterfall class
    def test_instance(self):
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
        self.assertTrue(len(Image.objects.all()) == 0)

    def test_all_photos(self):
        self.waterfall.save()
        photos = Image.all_photos()
        self.assertTrue(len(photos) > 0)

    def test_filter_by_categories(self):
        self.waterfall.save()
        images = Image.filter_by_categories(self.wild)
        self.assertTrue(len(images) > 0)

    def test_filter_by_location(self):
        self.waterfall.save()
        images = Image.filter_by_location(self.nairobi)
        self.assertTrue(len(images) > 0)

    def test_filter_by_search_term(self):
        self.waterfall.save()
        images = Image.filter_by_search_term('waterfall')
        self.assertTrue(len(images) > 0)
