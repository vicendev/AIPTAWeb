from django.urls import path
from . import views

urlpatterns = [
    path('publish/', views.publish, name="publish"),
    path('clinical-ofice/', views.clinical, name="clinical-office"),
    path('history/', views.history, name="history"),
]
