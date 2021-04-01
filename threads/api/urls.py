from django.conf.urls import url
from django.urls import include, path
from django.contrib import admin

from .views import (
    ThreadListAPIView,
    ThreadCreateAPIView,
    ThreadDetailAPIView,
    ThreadUpdateAPIView,
    ThreadDeleteAPIView,
    QueryThreadsApiView,
    QueryThreadMetaDataView,
)

urlpatterns = [
    path('', ThreadListAPIView.as_view(), name='user-list'),
    path('create/', ThreadCreateAPIView.as_view(), name='thread-create'),
    path('<int:pk>/', ThreadDetailAPIView.as_view(), name='thread-detail'),
    path('<int:pk>/edit/', ThreadUpdateAPIView.as_view(), name='thread-update'),
    path('<int:pk>/delete/', ThreadDeleteAPIView.as_view(), name='thread-delete'),
    path('getThreads/<int:forum_id>/',
         QueryThreadsApiView.get, name="get-threads"),
    path('getThreadMetaData/<int:thread_id>/',
         QueryThreadMetaDataView.get, name="get-threadmetadata"),
]
