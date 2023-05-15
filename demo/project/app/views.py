from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    msg="<h1>Home</h1>"
    return HttpResponse(msg)

def html(request):
    return render(request, 'home.html',{'name': 'rahul'})