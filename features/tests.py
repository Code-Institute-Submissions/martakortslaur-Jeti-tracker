from django.test import TestCase
from .models import Feature


class ProductTests(TestCase):
    """
    Here we'll define the tests that we'll run against our
    Product model
    """

    def test_str(self):
        test_name = Feature(name='A feature')
        self.assertEqual(str(test_name), 'A feature')
