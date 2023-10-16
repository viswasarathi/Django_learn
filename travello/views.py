from django.shortcuts import render
from .models import Destination
# Create your views here.

def index(request):
    dest1 = Destination()
    dest1.place = "India"
    dest1.city = "chennai - Marina beach"
    dest1.price = 999
    dest1.offer = True


    dest2 = Destination()
    dest2.place = "America"
    dest2.city = "New york"
    dest2.price = 1999
    dest2.offer = False

    dest3 = Destination()
    dest3.place = "Japan"
    dest3.city = "Tokyo"
    dest3.price = 1500
    dest3.offer = True

    dests = [dest1,dest2,dest3]



    return render(request,'index.html',{'dests':dests})

