from django.shortcuts import render
from django.http import HttpResponse
<<<<<<< HEAD

from rest_framework.views import APIView
from . models import *
from rest_framework.response import Response
from . serializer import *

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# Create your views here.

=======
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
# Create your views here.

def home (request):
	context = { "dummy":"1"}
	return render (request, 'SurfScopeForecast/temp.html',context)
>>>>>>> c645c202cb59f8da6c7ac19fae58204fb0482257

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

<<<<<<< HEAD
    def post(self, request):
        serializer = ReactSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
=======
def profile (request):
	return HttpResponse ('<h1>Include Profile here </h1>')


# @api_view(('GET',))
# @renderer_classes((TemplateHTMLRenderer, JSONRenderer))
# def temp(request):
#   success = "hello"
#   return Response(success, template_name='profile.html')
>>>>>>> c645c202cb59f8da6c7ac19fae58204fb0482257
