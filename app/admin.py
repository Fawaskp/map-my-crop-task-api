from django.contrib import admin
from .models import POI

class POIAdmin(admin.ModelAdmin):
    list_display = ('name', 'user')

admin.site.register(POI, POIAdmin)
