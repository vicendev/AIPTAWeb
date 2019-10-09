from django.shortcuts import render, get_list_or_404
from .models import Home
from about.models import About

# Create your views here.
def home(request):
    home = Home.objects.all()
    about = About.objects.all()
    return render(request, "home/home.html", {'home': home, 'about':about})

def home2(request):
    home = Home.objects.all()
    about = About.objects.all()
    return render(request, "ver2/home.html", {'home': home, 'about':about})
