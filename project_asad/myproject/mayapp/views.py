from django.shortcuts import render

from .models import Main

def asadbek(request):
    base = Main.objects.all()
    return render(request, 'main.html', {'ombor': base})