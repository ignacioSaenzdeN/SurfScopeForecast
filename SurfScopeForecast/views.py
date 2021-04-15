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

    # def put(self, request):
    #     secretsurfspot_data = request.data
    #     print(secretsurfspot_data)
    #     secretsurfspot_user = SurfingInfo.objects.filter(
    #         ID=u_id).update(secretList=secretsurfspot_data)
    #     return JsonResponse(secretsurfspot_user, safe=False)

    def post(self, request):
        serializer = SurfingInfoSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    # def putSss(self, request):
    #     an_id = request.GET.get('u_id', '')
    #     data = SurfingInfo.objects.filter(ID=an_id).values()[0]
    #     serializer = SurfingInfoSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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

    # elif request.method == 'POST':
    #     serializer = SurfingInfoSerializer(data=request.data)
    #     if serializer.is_valid(raise_exception=True):
    #         serializer.save()
    #     return Response(serializer.data)


class Surfboards(APIView):
    serializer_class = SurfboardsSerializer

    def post(self, request):
        serializer = SurfboardsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def get(self, request):
        boardQuestionData = request.GET.get('state', None)
        boardType = boardQuestionData.surfBoardSize

        return Response("response")


class user_wetsuit_post(APIView):
    serializer_class = UserWetsuitSerializer

    def post(self, request):
        surfing_info = SurfingInfo.objects.get(
            ID=request.data['user'])
        wetsuit_data = {'user': surfing_info.id}
        serializer = UserWetsuitSerializer(data=wetsuit_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def user_wetsuit(request, u_id):
    try:
        surfing_info_id = SurfingInfo.objects.get(
            ID=u_id).id
        UserWetsuit_query = UserWetsuit.objects.get(user_id=surfing_info_id)
    except UserWetsuit.DoesNotExist:
        return JsonResponse({'message': 'The user surfing info does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        userwetsuit_serializer = UserWetsuitSerializer(UserWetsuit_query)
        return JsonResponse(userwetsuit_serializer.data)

    elif request.method == 'PUT':
        userwetsuit_data = request.data
        userwetsuit_user = UserWetsuit.objects.filter(
            user_id=surfing_info_id).update(size=userwetsuit_data['size'], gender=userwetsuit_data['gender'], waterTemp=userwetsuit_data['waterTemp'], coldSensitivy=userwetsuit_data['coldSensitivy'],  zipperType=userwetsuit_data['zipperType'],  productUrl=userwetsuit_data['productUrl'])
        return JsonResponse(userwetsuit_user, safe=False)


class user_surfboard_post(APIView):
    serializer_class = UserSurfboardSerializer

    def post(self, request):
        surfing_info = SurfingInfo.objects.get(
            ID=request.data['user'])
        surfboard_data = {'user': surfing_info.id}
        serializer = UserSurfboardSerializer(data=surfboard_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def user_surfboard(request, u_id):
    try:
        surfing_info_id = SurfingInfo.objects.get(
            ID=u_id).id
        UserSurfboard_query = UserSurfboard.objects.get(
            user_id=surfing_info_id)
    except UserSurfBoardSerializer.DoesNotExist:
        return JsonResponse({'message': 'The user surfing info does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        usersurfboard_serializer = UserSurfboardSerializer(UserSurfboard_query)
        return JsonResponse(usersurfboard_serializer.data)

    elif request.method == 'PUT':
        usersurfboard_data = request.data
        usersurfboard_user = UserSurfboard.objects.filter(
            user_id=surfing_info_id).update(weight=usersurfboard_data['weight'], height=usersurfboard_data['height'], size=usersurfboard_data['size'], level=usersurfboard_data['level'],  waveSize=usersurfboard_data['waveSize'],  productUrl=userwetsuit_data['productUrl'])
        return JsonResponse(usersurfboard_user, safe=False)
