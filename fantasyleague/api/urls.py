from django.conf.urls import url
from django.urls import include, path
from django.contrib import admin
from . import views

# from .views import ()

urlpatterns = [
    path('surfers/',
         views.surfersView, name="surfersView"),
]
