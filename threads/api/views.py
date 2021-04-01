from threads.models import Thread
from posts.models import Post
from rest_framework import generics, views
from rest_framework.views import APIView
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)
# from .permissions import IsOwnerOrAdminOrReadOnly
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse

from .serializers import (
    ThreadListSerializer,
    ThreadCreateSerializer,
    ThreadDetailSerializer,
    ThreadUpdateSerializer,
    ThreadDeleteSerializer,
    QueryThreadsSerializer
)


class ThreadListAPIView(generics.ListAPIView):
    queryset = Thread.objects.all()
    serializer_class = ThreadListSerializer
    permission_classes = [AllowAny]


class ThreadCreateAPIView(generics.CreateAPIView):
    queryset = Thread.objects.all()
    serializer_class = ThreadCreateSerializer
    #permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]
    throttle_scope = 'create_thread'


class ThreadDetailAPIView(generics.RetrieveAPIView):
    queryset = Thread.objects.all()
    serializer_class = ThreadDetailSerializer
    permission_classes = [AllowAny]


class ThreadDeleteAPIView(generics.DestroyAPIView):
    queryset = Thread.objects.all()
    serializer_class = ThreadDeleteSerializer
    #permission_classes = [IsOwnerOrAdminOrReadOnly]
    permission_classes = [AllowAny]

    def delete(self, request, pk, format=None):
        posts = Post.objects.filter(thread_id=pk)
        posts.delete()
        thread = Thread.objects.filter(id=pk).delete()
        return Response(status=HTTP_200_OK)


class ThreadUpdateAPIView(generics.UpdateAPIView):
    # For now only admin can force update thread (change name, content, pin)
    queryset = Thread.objects.all()
    serializer_class = ThreadUpdateSerializer
    #permission_classes = [IsAdminUser]
    permission_classes = [AllowAny]


class QueryThreadsApiView(APIView):
    serializer_class = QueryThreadsSerializer

    def get(request, forum_id):
        tempDict = {}
        data = Thread.objects.filter(forum_id=forum_id).values()
        for i in range(len(data)):
            tempDict[i] = data[i]
        return JsonResponse(tempDict)


class QueryThreadMetaDataView(APIView):
    def get(request, thread_id):
        tempDict = {}
        postQuery = Post.objects.filter(thread_id=thread_id).values()
        if len(postQuery) != 0:
            latestPost = {'data': postQuery[len(postQuery) - 1]}
        else:
            latestPost = {'data': "Nothing has been posted in this topic."}

        print(latestPost)
        return JsonResponse(latestPost)
