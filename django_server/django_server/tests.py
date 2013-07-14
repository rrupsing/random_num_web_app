import unittest
from models import *
import config as config
import time
from tasks import clean
from django.utils import timezone
import datetime

class RandomNumberManagerTestCase(unittest.TestCase):
    """
    Test models functions
    """
    def setUp(self):
        pass

    def tearDown(self):
        RandomNumberProfile.objects.all().delete()

    def testCleanup(self):
        RandomNumberProfile.objects.create(range_start=10, range_end=25, create_date=timezone.now()-datetime.timedelta(days=2))
        clean()

        self.assertEquals(RandomNumberProfile.objects.all().count(), 0)



