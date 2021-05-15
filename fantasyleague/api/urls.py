from django.conf.urls import url
from django.urls import include, path
from django.contrib import admin
from . import views


# url to access this part of the application
urlpatterns = [
    path('surfers/',
         views.surfersView, name="surfersView"),
]
