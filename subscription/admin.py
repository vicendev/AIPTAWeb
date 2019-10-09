from django.contrib import admin
from .models import Subscription

# Register your models here.

class SubscriptionAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

admin.site.register(Subscription, SubscriptionAdmin)