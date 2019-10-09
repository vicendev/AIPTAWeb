from django.contrib import admin
from .models import Announcement

# Register your models here.
class AnnouncementAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Announcement, AnnouncementAdmin)