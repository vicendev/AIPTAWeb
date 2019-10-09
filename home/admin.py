from django.contrib import admin
from .models import Home

# Register your models here.
class HomeAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Home, HomeAdmin)