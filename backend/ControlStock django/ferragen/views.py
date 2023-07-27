from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hola(request):
	return HttpResponse('Hello world')

def adios(request):
	return HttpResponse('Bye world')

