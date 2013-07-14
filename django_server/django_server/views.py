from django.http import HttpResponse, HttpResponseForbidden, HttpResponseBadRequest
from django.core import serializers
from api import RandomManagerAPI

# ASSUMPTION random numbers are in the range of range_start, range_end inclusive

def generate_random(request):
    random_number_profile_id = None
    range_start = None
    range_end = None
    seed = None

    if request.GET.has_key('random_number_profile_id') and isinstance(request.GET.has_key('random_number_profile_id'), int):
        random_number_profile_id = int(request.GET['random_number_profile_id'])
    if request.GET.has_key('range_start') and isinstance(request.GET.has_key('range_start'), int):
        range_start = int(request.GET['range_start'])
    if request.GET.has_key('range_end') and isinstance(request.GET.has_key('range_end'), int):
        range_end = int(request.GET['range_end'])
    if request.GET.has_key('seed') and isinstance(request.GET.has_key('seed'), int):
        seed = int(request.GET['seed'])

    if random_number_profile_id is None and (range_start is None or range_end is None):
        return HttpResponseBadRequest("Must specify either a random_number_profile_id or start and end range parameter")

    random_api_manager = RandomManagerAPI()

    if random_number_profile_id is not None:
        return random_api_manager.generate_from_profile(random_number_profile_id=random_number_profile_id)
    else:
        return random_api_manager.generate(range_start=range_start, range_end=range_end, seed=seed)

def number_profile(request):
    random_number_profile_id = None
    range_start = None
    range_end = None
    seed = None

    if request.POST.has_key('random_number_profile_id') and isinstance(request.GET.has_key('random_number_profile_id'), int):
        random_number_profile_id = int(request.POST['random_number_profile_id'])
    if request.POST.has_key('range_start') and isinstance(request.GET.has_key('range_start'), int):
        range_start = int(request.POST['range_start'])
    if request.POST.has_key('range_end') and isinstance(request.GET.has_key('range_end'), int):
        range_end = int(request.POST['range_end'])
    if request.POST.has_key('seed') and isinstance(request.GET.has_key('seed'), int):
        seed = int(request.POST['seed'])

    # proper way to do this is to detect the HTTP DELETE command and process, however I didn't have time to integrate the django rest library
    # so instead I assume if they are posting with a random_number_profile_id then it is a DELETE command
    if random_number_profile_id is None and (range_start is None or range_end is None):
        return HttpResponseBadRequest("Must specify either a random_number_profile_id or start and end range parameter")

    random_api_manager = RandomManagerAPI()

    if random_number_profile_id is not None:
        return random_api_manager.delete_random_number_profile(random_number_profile_id=random_number_profile_id)
    else:
        return random_api_manager.create_random_number_profile(range_start=range_start, range_end=range_end, seed=seed)

