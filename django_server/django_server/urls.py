from django.conf.urls import patterns, include, url
"""
from rest_framework import viewsets, routers

# ViewSets define the view behavior.
class RandomNumberProfileViewSet(viewsets.ModelViewSet):
    model = RandomNumberProfile

# Routers provide an easy way of automatically determining the URL conf
router = routers.DefaultRouter()
router.register(r'random_number_profiles', RandomNumberProfileViewSet)
"""
urlpatterns = patterns('',
    # Examples:
    #    url(r'^', include(router.urls)),
    url(r'^number_profile', 'django_server.views.number_profile'),
    url(r'^generate_random', 'django_server.views.generate_random'),
    url(r'^room/?', include('django_server.room.urls')),

)
