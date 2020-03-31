from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return render(request, 'flatshare/index.html')

def about(request):
    return render(request, 'flatshare/about.html')

def login(request):
    return HttpResponse("place holder login page")

def signup(request):
    return HttpResponse("place holder signup page")

def addflat(request):
    return HttpResponse("place holder addflat page")

def findflat(request):
    return HttpResponse("place holder findflat page")
