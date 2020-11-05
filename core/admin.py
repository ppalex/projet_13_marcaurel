from django.contrib import admin

# Register your models here.
from django.contrib.gis.admin import OSMGeoAdmin

from .models.player import Player
from .models.location import Location

# admin.site.register(Player)

@admin.register(Player)
class PlayerAdmin(OSMGeoAdmin):
    pass

@admin.register(Location)
class LocationAdmin(OSMGeoAdmin):
    pass