from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
# Create your views here.

def home (request):
	context = { "dummy":"1"}
	return render (request, 'SurfScopeForecast/temp.html',context)

def fantasyLeague (request):
	return HttpResponse ('<h1>Include FantasyLeague here </h1>')

def forum (request):
	return HttpResponse ('<h1>Include Forum here </h1>')

def maps (request):
	return HttpResponse ('<h1>Include maps here </h1>')

def profile (request):
	return HttpResponse ('<h1>Include Profile here </h1>')


# @api_view(('GET',))
# @renderer_classes((TemplateHTMLRenderer, JSONRenderer))
# def temp(request):
#   success = "hello"
#   return Response(success, template_name='profile.html')