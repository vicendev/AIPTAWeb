from django.contrib import admin
from .models import Formation

# Register your models here.

class FormationAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Formation, FormationAdmin)