from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    #    url(r'^', include(router.urls)),
    url(r'^number_profile', 'django_server.views.number_profile'),
    url(r'^generate_random', 'django_server.views.generate_random'),

)
