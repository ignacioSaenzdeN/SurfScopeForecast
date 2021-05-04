# from django.urls import path, include
from . import views
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from SurfScopeForecast.views import *
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('', views.index, name='surfscopeforecast'),
    path('fantasyleague/', views.index, name='SSF-FantasyLeague'),
    path('forum/', views.index, name='SSF-forum'),
    path('maps/', views.index, name='SSF-maps'),
    path('profile/', views.index, name='SSF-profile'),
    path('wel/', ReactView.as_view(), name="something"),
    path('surfingInfo/<u_id>/',
         views.user_surfinginfo, name="something"),
    path('userfantasyleague/<u_id>/',
         views.user_fantasyleague, name="user_fantasyleague"),
    path('getTopFive/', views.getTopFive, name="getTopFive"),
    path('surfingInfo/',
         SurfingInfoView.as_view(), name="something"),
    #path('getSingle/', SurfingInfoView.getSingle, name="getInfo"),
    #path('putSss/', SurfingInfoView.putSss, name="sss"),
    path('surfboards/', Surfboards.as_view(), name="surfboards"),
    #path('wetsuits/', Wetsuits.as_view(), name="wetsuits")
    path('userwetsuit/<u_id>/',
         views.user_wetsuit, name="userwetsuit"),
    path('userwetsuit/',
         user_wetsuit_post.as_view(), name="userwetsuit"),
    path('usersurfboard/<u_id>/',
         views.user_surfboard, name="usersurfboard"),
    path('usersurfboard/',
         user_surfboard_post.as_view(), name="usersurfboard"),




]
