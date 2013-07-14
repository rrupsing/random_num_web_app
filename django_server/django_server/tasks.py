import time
from celery import task
from models import RandomNumberProfile
from django.utils import timezone
import config as config
import datetime

@task.task(ignore_result=True)
def clean():
    RandomNumberProfile.objects.filter(create_date__lt=timezone.now()-datetime.timedelta(seconds=config.RANDOM_NUMBER_PROFILE_EXPIRY_TIME)).delete()