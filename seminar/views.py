from django.shortcuts import render
from .models import Seminar

# Create your views here.

def seminars(request):
    seminars = Seminar.objects.all()
    return render(request, "seminar/seminar.html", {'seminars':seminars})