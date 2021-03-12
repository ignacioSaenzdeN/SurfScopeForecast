from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . models import *
from . serializer import *
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.core.serializers import serialize
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.db.models.functions import Concat

# Create your views here.


def home(request):
    return HttpResponse('<h1> Include Homepage here </h1>')


def fantasyLeague(request):
    return HttpResponse('<h1>Include FantasyLeague here </h1>')


def forum(request):
    return HttpResponse('<h1>Include Forum here </h1>')


def maps(request):
    return HttpResponse('<h1>Include maps here </h1>')


def profile(request):
    return HttpResponse('<h1>Include Profile here </h1>')


class ReactView(APIView):

    serializer_class = ReactSerializer

    def get(self, request):
        detail = [{'name': detail.name, 'detail': detail.detail, 'newfield': detail.newfield}
                  for detail in Blackbox.objects.all()]

        return Response(detail)

    def post(self, request):
        serializer = ReactSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


class SurfingInfoView(APIView):
    serializer_class = SurfingInfoSerializer

    # def get(self, request):
    #     detail = [{'ID': detail.ID, 'secretList': detail.secretList, 'fantasyLeague': detail.fantasyLeague,
    #                'alerts': detail.alerts} for detail in SurfingInfo.objects.all()]
    #     return Response(detail)

#     def post(self, request):
#         serializer = SurfingInfoSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)

#     def putSss(self, request):
#         an_id = request.GET.get('u_id', '')
#         data = SurfingInfo.objects.filter(ID=an_id).values()[0]
#         serializer = SurfingInfoSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def getSingle(request):
    #     serializer = SurfingInfoSerializer
    #     an_id = request.GET.get('u_id', '')
    #     data = SurfingInfo.objects.filter(ID=an_id).values()
    #     print(data)
    #     return JsonResponse(data[0])


@api_view(['GET', 'PUT', 'DELETE'])
def user_surfinginfo(request, u_id):
    try:
        surfinginfo = SurfingInfo.objects.get(ID=u_id)
    except SurfingInfo.DoesNotExist:
        return JsonResponse({'message': 'The user surfing info does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        print(surfinginfo.secretList)
        surfinginfo_serializer = SurfingInfoSerializer(surfinginfo)
        return JsonResponse(surfinginfo_serializer.data)

    elif request.method == 'PUT':
        secretsurfspot_data = request.data
        print(secretsurfspot_data)
        secretsurfspot_user = SurfingInfo.objects.filter(
            ID=u_id).update(secretList=secretsurfspot_data)
        return JsonResponse(secretsurfspot_user, safe=False)
