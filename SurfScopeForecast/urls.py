# from django.urls import path, include
from . import views
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from SurfScopeForecast.views import *
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('', views.home, name='SSF-homepage'),
    path('fantasyLeague/', views.fantasyLeague, name='SSF-FantasyLeague'),
    path('forum/', views.forum, name='SSF-forum'),
    path('maps/', views.maps, name='SSF-maps'),
    path('profile/', views.profile, name='SSF-profile'),
    path('wel/', ReactView.as_view(), name="something"),
    path('surfingInfo/', SurfingInfoView.as_view(), name="something"),
    path('getSingle/<str:temp>', views.getSingle, name="getInfo"),
]
