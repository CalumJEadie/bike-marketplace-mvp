"""
python manage.py test bike_marketplace_mvp
"""

from django.test import TestCase

from models import Bike, Seller

class BikeTest(TestCase):

    def test_bikepedia_url(self):

        seller = Seller()

        bike = Bike(
            seller=seller,
            name="Trek 7100"
        )
        print bike.bikepedia_url