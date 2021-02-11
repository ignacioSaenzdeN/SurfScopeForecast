from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from . models import *
from rest_framework.response import Response
from . serializer import *
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.core.serializers import serialize
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

	def get (self,request):
		detail = [{'ID': detail.ID, 'secretList':detail.secretList, 'fantasyLeague':detail.fantasyLeague,
		 'alerts':detail.alerts} for detail in SurfingInfo.objects.all()]
		return Response(detail)

	def post (self,request):
		serializer = SurfingInfoSerializer(data= request.data)
		if serializer.is_valid(raise_exception=True):
			serializer.save()
			return Response(serializer.data)

	
def getSingle(request,temp):
	serializer= SurfingInfoSerializer
	data = SurfingInfo.objects.filter(ID=temp).values()
	print(data)
	return JsonResponse(data[0])