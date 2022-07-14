from django.shortcuts import render
from .models import *

def main(request):
    base = Main.objects.all()
    a = [
        {'name': 'Asadbek', 'age': 17, 'number': 998931418286}
    ]
    print(base)
    return render(request, 'base_1.html', {'ombor': base, 'print': a})
