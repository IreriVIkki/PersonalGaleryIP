from django.test import TestCase
from .models import Image, categories, Location


#  test categories class
class TestCategories (TestCase):
    def setUp(self):
        self.nature = categories(name='nature')

    def test_instance(self):
        self.nature.save()
        self.assertTrue(isinstance(self.nature, categories))


class TestLocationClass (TestCase):
    def setup(self):
        self.nairobi = Location(location='nairobi')

    def test_instance(self):
        self.assertTrue(isinstance(self.nairobi, Location))


class ImageTest(TestCase):

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
    def test_instance(self):
        self.waterfall.save()
        self.assertTrue(isinstance(self.waterfall, Location))

    # def test_category_instance(self):
    #     self.waterfall.save()
    #     self.assertTrue(isinstance(self.wild, categories))
    #     self.assertTrue(isinstance(self.nature, categories))

    # def test_location_instance(self):
    #     self.waterfall.save()
    #     self.assertTrue(isinstance(self.nairobi, Location))

    # def test_delete_image(self):
    #     self.waterfall.save()
    #     self.waterfall.delete()
    #     self.assertTrue(len(Image.objects.all()) == 0)

    # def test_delete_by_id(self):
    #     self.waterfall.save()
    #     Image.delete_by_id(self.waterfall.id)
    #     self.assertIsNone(self.waterfall, None)

    #     self.waterfall.save()
    #     self.assertEqual(len(self.waterfall.categoies.all()), 4)
