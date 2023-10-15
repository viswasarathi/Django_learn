from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,'home.html',{'name':'viswa'})

def add(request):
    x = request.GET['n1']
    y = request.GET['n2']
    res = int(x) + int(y)
    return render(request,'result.html',{'result':res})