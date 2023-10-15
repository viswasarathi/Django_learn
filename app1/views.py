from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt 
# Create your views here.

def index(request):
    return render(request,'home.html',{'name':'viswa'})

@csrf_exempt
def add(request):
    x = request.POST['n1']
    y = request.POST['n2']
    res = int(x) + int(y)
    return render(request,'result.html',{'result':res})