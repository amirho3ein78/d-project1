from django.shortcuts import render,HttpResponse

# Create your views here.

def HomePageView(request):
    return HttpResponse("helloworld")

def AboutPageView(request):
    return HttpResponse("why do you want to know mee?")