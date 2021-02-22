from django.shortcuts import render,HttpResponse
from django.views.generic import TemplateView

# Create your views here.
'''
def HomePageView(request):
    if (request.method=='GET'):
        context={
            "messege":"helloworld"
        }
        return render(request,'pages/index.html',context)


def AboutPageView(request):
    if (request.method=='GET'):
        context={
            "messege":"why do you want to know mee?"
        }
        return render(request,'pages/about.html',context)
'''

class AboutPageView(TemplateView):
    template_name="pages/about.html"

class HomePageView(TemplateView):
    template_name="pages/index.html"