from threads.models import Thread
from posts.models import Post
from forums.models import Forum
from rest_framework import generics, views
from rest_framework.views import APIView
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)

from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse

from .serializers import (
    ForumListSerializer,
    ForumCreateDeleteSerializer,
    ForumUpdateSerializer,
    ForumDetailSerializer
)


class ForumListAPIView(generics.ListAPIView):
    queryset = Forum.objects.all()
    serializer_class = ForumListSerializer
    permission_classes = [AllowAny]


class ForumCreateAPIView(generics.CreateAPIView):
    serializer_class = ForumCreateDeleteSerializer
    queryset = Forum.objects.all()
    #permission_classes = [IsAdminUser]
    permission_classes = [AllowAny]


class ForumDetailAPIView(generics.RetrieveAPIView):
    queryset = Forum.objects.all()
    serializer_class = ForumDetailSerializer
    permission_classes = [AllowAny]
    lookup_field = 'slug'


class ForumDeleteAPIView(generics.DestroyAPIView):
    queryset = Forum.objects.all()
    serializer_class = ForumCreateDeleteSerializer
    #permission_classes = [IsAdminUser]
    permission_classes = [AllowAny]
    lookup_field = 'slug'


class ForumUpdateAPIView(generics.UpdateAPIView):
    queryset = Forum.objects.all()
    serializer_class = ForumUpdateSerializer
    #permission_classes = [IsAdminUser]
    permission_classes = [AllowAny]
    lookup_field = 'slug'

# We get the last post and we get the last post in the most recent thread as well as the date it was posted


class QueryForumMetadata(APIView):
    def get(request, forum_id):
        allThreads = Thread.objects.filter(forum_id=forum_id).values()
        i = 0
        if len(allThreads) is 0:
            forumPost = {'data': 'There are no topics in this forum.'}
            return JsonResponse(forumPost)
        newstThreadId = allThreads[i]['id']
        allPosts = Post.objects.filter(thread_id=newstThreadId).values()
        while len(allPosts) == 0:
            if len(allThreads) > (i + 1):
                i += 1
                newstThreadId = allThreads[i]['id']
                allPosts = Post.objects.filter(
                    thread_id=newstThreadId).values()
            else:
                forumPost = {'data': 'There are no posts in this forum.'}
                return JsonResponse(forumPost)
        forumPost = {'data': allPosts[len(allPosts) - 1]}
        return JsonResponse(forumPost)
