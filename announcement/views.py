from django.shortcuts import render
from .models import Announcement

# Create your views here.
def announcement(request):
    announcement = Announcement.objects.all()
    return render(request, "announcement/announcement.html", {'announcement':announcement})