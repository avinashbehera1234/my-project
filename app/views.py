from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first(request):
    return HttpResponse('This Is Our First View Function')
def propose(request):
    return HttpResponse('<marquee>yes i love u too</marquee>')
def rejection(request):
    return HttpResponse('<h1>sorry i have a girlfriend')
