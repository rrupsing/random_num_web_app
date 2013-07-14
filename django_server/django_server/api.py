from models import RandomNumberProfile
import random
import config as config
from django.utils import timezone
import datetime
from packets.plain_response import HttpResponsePlain

class RandomManagerAPI(object):

    def generate(self, range_start, range_end, seed=None):
        if seed is not None:
            random.seed(seed)
        return HttpResponsePlain(random.randint(range_start, range_end))

    def generate_from_profile(self, random_number_profile_id):

        try:
            random_number_profile = RandomNumberProfile.objects.get(id=random_number_profile_id)
        except RandomNumberProfile.DoesNotExist:
            raise Exception("RandomNumberProfile not found!")

        if random_number_profile.create_date < timezone.now() - datetime.timedelta(seconds=config.RANDOM_NUMBER_PROFILE_EXPIRY_TIME):
            raise Exception("RandomNumberProfile requested has expired")

        return self.generate(range_start=random_number_profile.range_start, range_end=random_number_profile.range_end, seed=random_number_profile.seed)

    def create_random_number_profile(self, range_start, range_end, seed=None):
        random_number_profile = RandomNumberProfile.objects.create(range_start=range_start, range_end=range_end, seed=seed)
        return HttpResponsePlain(random_number_profile.id)

    def delete_random_number_profile(self, random_number_profile_id):
        # if it is not found, doesn't matter
        RandomNumberProfile.objects.filter(id=random_number_profile_id).delete()
        return HttpResponsePlain('')


