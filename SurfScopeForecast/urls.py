# from django.urls import path, include
from . import views

<<<<<<< HEAD
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from SurfScopeForecast.views import *
from rest_framework.routers import DefaultRouter
=======
urlpatterns = [
    path('', views.home, name ='SSF-homepage'),
    path('fantasyLeague/', views.fantasyLeague, name ='SSF-FantasyLeague'),
    path('forum/', views.forum, name ='SSF-forum'),
    path('maps/', views.maps, name ='SSF-maps'),
    path('profile/', views.profile, name ='SSF-profile'),
    # path('test', views.temp, name = 'temp'),
>>>>>>> c645c202cb59f8da6c7ac19fae58204fb0482257

urlpatterns = [
    path('', views.home, name='SSF-homepage'),
    path('fantasyLeague/', views.fantasyLeague, name='SSF-FantasyLeague'),
    path('forum/', views.forum, name='SSF-forum'),
    path('maps/', views.maps, name='SSF-maps'),
    path('profile/', views.profile, name='SSF-profile'),
    path('wel/', ReactView.as_view(), name="something"),
]
