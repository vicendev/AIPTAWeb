from django import forms
from .models import Subscription

class SubscriptionForm(forms.ModelForm):

    name = forms.CharField(label='Nombre', required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label='Email', required=True, widget=forms.EmailInput(attrs={'class':'form-control'}))
    phone = forms.IntegerField(label='Teléfono', required=True, widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = Subscription
        fields = ['name','email','phone']