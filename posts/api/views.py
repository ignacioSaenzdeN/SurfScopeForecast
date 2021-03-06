from posts.models import Post
from threads.models import Thread
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
    PostListSerializer,
    PostCreateSerializer,
    PostDetailSerializer,
    PostUpdateSerializer,
    PostDeleteSerializer,
    QueryPostsSerializer
)


class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    # permission_classes = [IsAdminUser]


class PostCreateAPIView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]
    throttle_scope = 'create_post'


class PostDetailAPIView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    permission_classes = [AllowAny]


class PostDeleteAPIView(generics.DestroyAPIView):
    # For now only admin can delete post,
    # because if user keep on deleting post doesn't make sense
    queryset = Post.objects.all()
    serializer_class = PostDeleteSerializer
    # permission_classes = [IsOwnerOrAdminOrReadOnly]
    permission_classes = [AllowAny]

    def delete(self, request, pk, format=None):
        # try:
        post = Post.objects.get(pk=pk)

        thread_id = post.thread_id

        post.delete()

        # # since we deleted a post, we now check the latest post
        # latest_post = Post.objects.filter(
        #     thread=thread).order_by('-created_at').first()

        # update the deleted post's thread last_activity
        # if latest_post is None:
        #     thread.last_activity = thread.created_at
        # else:
        #     thread.last_activity = latest_post.created_at
        # thread.save()
        # Response(status=HTTP_200_OK)
        tempDict = {}
        data = Post.objects.filter(thread_id=thread_id).values()
        for i in range(len(data)):
            tempDict[i] = data[i]

        return JsonResponse(tempDict)

        # except:
        #     return Response(status=HTTP_400_BAD_REQUEST)


class PostUpdateAPIView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostUpdateSerializer
    # permission_classes = [IsOwnerOrAdminOrReadOnly]


class QueryPostsApiView(APIView):
    print('thread_id')
    serializer_class = QueryPostsSerializer
    print("after serializer")

    def get(self, request, thread_id):
        print('thread_id')
        # print(thread_id)
        #forumid_ = request.GET.get('forum_id', '')
        tempDict = {}
        data = Post.objects.filter(thread_id=thread_id).values()
        print(data)
        for i in range(len(data)):
            tempDict[i] = data[i]
        return JsonResponse(tempDict)
