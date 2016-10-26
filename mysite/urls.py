"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from mysite.views import current_datetime, hours_ahead, evan

from rest_framework import routers, serializers, viewsets

from jam.models import Artists, Album
from jam.API_Config import *
from jam.jam_api import *
from jam.views import *

############################
# API CONFIGURATION SETTINGS
############################

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'Artist', ArtistViewSet)

############
#       URLS
############

urlpatterns = [
    # ADMIN PAGES
    url(r'^admin/', admin.site.urls),   # imported
    # url(r'^hello/$', hello),          # Hello, World
    # url(r'^time/add_artist/([a-z0-9_-]{1,100})$', add_artist), # Adding Artist to DB from Spotify API
    # url(r'^time/add_album/([A-Za-z0-9_-]{1,100})$', add_album), # Adding Album to DB from Spotify API
    # url(r'^time/jam_out/add_review/$', add_review),

    
    # API Pages
    url(r'^time/api/artists/([A-Za-z0-9_-]{1,10000})/$', artist_detail),
    url(r'^time/api/features/$', features),

    # PITCHFORK API
    url(r'^time/api/pitchfork/search/([A-Za-z0-9_-]{1,10000})/([A-Za-z0-9_-]{1,10000})/$', search),
    
    # If you're intending to use the browsable API you'll probably also want to add REST framework's 
    # login and logout views. Add the following to your root urls.py file:
    # url(r'^', include(router.urls)),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),


    # WEB PAGES
    url(r'^$', current_datetime),
    url(r'^time/$', current_datetime),
    url(r'^time/evan/$', evan),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),

    # JAM PAGES
    url(r'^time/jam_out/$', lets_jam),
    url(r'^time/jam_out$', lets_jam),
    url(r'^time/jam_out/recommend/$', lets_jam_recommend),
    url(r'^time/jam_out/([A-Za-z0-9_-]{1,100})/$', lets_jam_review),

]

# Importing Static File URLS
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
