from ast import Delete
from random import random
from django.shortcuts import render

from .models import Main, Tovar

def base(request):
    base_1 = Tovar.objects.all()
    return render(request,'base.html', {'base_1': base_1})

def ac(request, raqam):
    base = Tovar.objects.get(slug=raqam)
    return render(request, 'base_1.html', {'base': base})