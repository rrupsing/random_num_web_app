from django.db import models
from django.utils import timezone
import datetime
import random as random

class RandomNumberProfile(models.Model):
    # beginning of the random number range
    range_start = models.IntegerField()
    # end of the random number range
    range_end = models.IntegerField()
    # random seed
    seed = models.IntegerField(blank=True, null=True)
    # create date
    create_date = models.DateTimeField(default=timezone.now())
