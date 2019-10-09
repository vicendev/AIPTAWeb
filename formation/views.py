from django.shortcuts import render
from .models import Formation

# Create your views here.

def formations(request):
    formations = Formation.objects.all()
    return render(request, "formation/formation.html", {'formations':formations})

