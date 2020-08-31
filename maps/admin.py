from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin

from maps.models import Entry


@admin.register(Entry)
class EntryAdmin(OSMGeoAdmin):
    default_lon = 1263000
    default_lat = 5542000
    default_zoom = 12
