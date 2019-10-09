from django.shortcuts import render, redirect
from django.urls import reverse

from subscription.models import Subscription
from subscription.forms import SubscriptionForm
# Create your views here.

def publish(request):
    # add suscription #
    if request.method == 'POST':
        subscriptionForm = SubscriptionForm(request.POST)

        if subscriptionForm.is_valid():
            subscriptionForm.save()

            return redirect(reverse('publish'))
    # end add suscription #

    else: 
        subscriptionForm = SubscriptionForm()
    return render(request, "core/publish.html", {'subscriptionForm':subscriptionForm})

def clinical(request):
    return render(request, "core/clinical_office.html")

def history(request):
    return render(request, "core/history.html")
