from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home (request):
	return HttpResponse ('<h1> Include Homepage here </h1>')

def fantasyLeague (request):
	return HttpResponse ('<h1>Include FantasyLeague here </h1>')

def forum (request):
	return HttpResponse ('<h1>Include Forum here </h1>')

def maps (request):
	return HttpResponse ('<h1>Include maps here </h1>')

def profile (request):
	return HttpResponse ('<h1>Include Profile here </h1>')