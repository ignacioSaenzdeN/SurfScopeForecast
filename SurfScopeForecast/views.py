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
from django.forms.models import model_to_dict
from django.db.models import IntegerField
from django.db.models.functions import Cast
from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache

index = never_cache(TemplateView.as_view(template_name='index.html'))

# Not used


def home(request):
    return HttpResponse('<h1> Include Homepage here </h1>')

# Not used


def fantasyLeague(request):
    return HttpResponse('<h1>Include FantasyLeague here </h1>')

# Not used


def forum(request):
    return HttpResponse('<h1>Include Forum here </h1>')

# Not used


def maps(request):
    return HttpResponse('<h1>Include maps here </h1>')

# Not used


def profile(request):
    return HttpResponse('<h1>Include Profile here </h1>')

# Currently not being used


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

# SurfingInfoView is currently not being used


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

# user_surfinginfo is used to retrieve and update surfinginfo models


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

# Surfboards handles the views related to surfboards


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

# user_wetsuit_post handles the views used for the wetsuits


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

# user_wetsuit is used to update and retrieve data
# related to the wetsuit


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

# user_surfboard_post is used to post surfboard data


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

# user_wetsuit is used to update and retrieve data
# related to the wetsuit


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
            user_id=surfing_info_id).update(weight=usersurfboard_data['weight'], height=usersurfboard_data['height'], size=usersurfboard_data['size'], level=usersurfboard_data['level'],  waveSize=usersurfboard_data['waveSize'],  productUrl=usersurfboard_data['productUrl'])
        return JsonResponse(usersurfboard_user, safe=False)

# user_fantasyleague is used to handle the gets and
# puts related to the fantasy league


@api_view(['GET', 'PUT', 'DELETE'])
def user_fantasyleague(request, u_id):
    try:
        surfinginfo = SurfingInfo.objects.get(ID=u_id)
    except SurfingInfo.DoesNotExist:
        return JsonResponse({'message': 'The user surfing info does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        print(SurfingInfoSerializer(surfinginfo))
        surfinginfo_serializer = SurfingInfoSerializer(surfinginfo)
        return JsonResponse(eval(surfinginfo_serializer.data["fantasyLeague"]), safe=False)

    elif request.method == 'PUT':
        selectedTeam = request.data["selectedTeam"]
        totalTeamScore = request.data["totalScore"]

        fantasyLeague_user = SurfingInfo.objects.filter(
            ID=u_id).update(fantasyLeague=selectedTeam, totalTeamScore=totalTeamScore)

        return JsonResponse(fantasyLeague_user, safe=False)

# getTopFive retrieves the top 5 teams in the fantasy league


@api_view(['GET', 'PUT', 'DELETE'])
def getTopFive(request):
    try:
        surfinginfo = SurfingInfo.objects.all()
        #surfinginfo = SurfingInfo.objects.all().order_by("-totalTeamScore")
        #surfinginfo = SurfingInfo.objects.extra(select={'totalTeamScore': 'CAST(totalTeamScore AS INTEGER)'},order_by=['totalTeamScore'])
        #surfinginfo = SurfingInfo.objects.annotate(as_float=Cast('totalTeamScore', IntegerField()))
        # surfinginfo = SurfingInfo.objects.annotate(as_float=Cast(
        #     'totalTeamScore', FloatField())).order_by("-totalTeamScore")

    except SurfingInfo.DoesNotExist:
        return JsonResponse({'message': 'The user surfing info does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        print(surfinginfo)
        surfingInfoList = []
        surfingInfo = list(surfinginfo)
        tempElement = {}
        for element in surfinginfo:
            tempElement = model_to_dict(element)
            print(tempElement['totalTeamScore'])
            if tempElement['totalTeamScore'] != '' and tempElement['totalTeamScore'] != '0':

                tempElement['fantasyLeague'] = eval(
                    tempElement['fantasyLeague'])
                tempElement['totalTeamScore'] = int(
                    tempElement['totalTeamScore'])
                surfingInfoList.append(tempElement)
        surfingInfoList.sort(
            key=lambda i: i['totalTeamScore'], reverse=True)
        print(surfingInfoList)
        return JsonResponse(surfingInfoList[:5], safe=False)
