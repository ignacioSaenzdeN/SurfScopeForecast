from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name ='SSF-homepage'),
    path('fantasyLeague/', views.fantasyLeague, name ='SSF-FantasyLeague'),
    path('forum/', views.forum, name ='SSF-forum'),
    path('maps/', views.maps, name ='SSF-maps'),
    path('profile/', views.profile, name ='SSF-profile'),

]