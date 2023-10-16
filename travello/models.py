from django.db import models

# Create your models here.

class Destination:
    id:int
    place:str
    city:str
    price:int
    offer : bool