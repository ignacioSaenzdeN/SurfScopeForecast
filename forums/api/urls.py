from django.conf.urls import url
from django.urls import include, path
from django.contrib import admin

from .views import (
    ForumCreateAPIView,
    ForumDetailAPIView,
    ForumListAPIView,
    ForumDeleteAPIView,
    ForumUpdateAPIView,
    QueryForumMetadata,
)
# urls used for topics related to forums
urlpatterns = [
    path('', ForumListAPIView.as_view(), name='forum-list'),
    path('create/', ForumCreateAPIView.as_view(), name='forum-create'),
    path('<slug:slug>/', ForumDetailAPIView.as_view(), name='forum-detail'),
    path('<slug:slug>/edit/', ForumUpdateAPIView.as_view(), name='forum-update'),
    path('<slug:slug>/delete/', ForumDeleteAPIView.as_view(), name='forum-delete'),
    path('getMetadata/<int:forum_id>/',
         QueryForumMetadata.get, name="get-metadata"),
]
