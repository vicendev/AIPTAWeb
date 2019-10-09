from django.contrib import admin
from .models import Seminar

# Register your models here.

class SeminarAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Seminar, SeminarAdmin)